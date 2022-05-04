
from unicodedata import category
from flask import Blueprint, make_response, render_template, request, current_app, url_for, flash, redirect, abort
from app.utils import redirect_back
from flask_login import current_user

from app.models import Category, Post, Comment
from app.forms import *
from app.extensions import db 
from app.emails import *


blog_bp = Blueprint('blog', __name__, template_folder = 'templates')  



@blog_bp.route('/', defaults = {'page':1})
@blog_bp.route('/page/<int:page>')  # ip/
def index(page):  # 渲染主页模板的index视图
    # posts = Post.query.order_by(Post.timestamp.desc())
    # page = request.args.get('page', 1, type = int)  # /home#page=4
    per_page = current_app.config['BLUEBLOG_POST_PER_PAGE']
    pagination = Post.query.order_by(Post.timestamp.desc()).paginate(page, per_page=per_page)
    posts = pagination.items
    return render_template('blog/index.html', pagination=pagination, posts = posts)


@blog_bp.route('/about')
def about():
    return render_template('blog/about.html')


@blog_bp.route('/category/<int:category_id>')
def show_category(category_id):
    category = Category.query.get_or_404(category_id)
    page = request.args.get('page', 1, type = int)
    per_page =current_app.config['BLUEBLOG_POST_PER_PAGE']
    pagination = Post.query.with_parent(category).order_by(Post.timestamp.desc()).paginate(page, per_page)
    posts = pagination.items    
    return render_template('blog/category.html', category=category, pagination = pagination, posts=posts)


@blog_bp.route('/post/<post_id>', methods=['GET', 'POST']) 
def show_post(post_id): 
    # post, pagination for comments, comments, category


    # 'blog.show_post', post_id=comment.post_id, reply=comment_id, author=comment.author) + '#comment-form')
    post = Post.query.get_or_404(post_id)
    page = request.args.get('page', 1, type = int)
    per_page = current_app.config['BLUEBLOG_COMMENT_PER_PAGE']
    pagination = Comment.query.with_parent(post).filter_by(reviewed = True).order_by(Comment.timestamp.asc()).paginate(page, per_page)
    comments = pagination.items
    if current_user.is_authenticated:
        form = AdminCommentForm()
        form.author.data = current_user.name
        form.email.data = current_app.config['BLUEBLOG_EMAIL']
        form.site.data = url_for('blog.index')
        from_admin = True
        reviewed = True
    else:
        form = CommentForm()
        from_admin = False
        reviewed = False 

    if form.validate_on_submit():
        author = form.author.data 
        email = form.email.data 
        site = form.site.data 
        body = form.body.data 
        comment = Comment(author = author, email = email, site = site, \
        body = body, from_admin = from_admin, post = post, reviewed = reviewed)
        replied_id = request.args.get('reply')
        if replied_id:
            replied_comment = Comment.query.get_or_404(replied_id)
            comment.replied = replied_comment
            send_new_reply_email(replied_comment)
        db.session.add(comment)
        db.session.commit()

        if current_user.is_authenticated:
            flash('Comment published!', 'success')
        else:
            
            send_new_comment_email(post)
            flash('Thanks! Your comment would be published after reviewed!', 'info')
        return redirect(url_for('blog.show_post', post_id=post_id))
    return render_template('blog/post.html', post=post, pagination=pagination, form = form, comments=comments)


@blog_bp.route('/reply/comment/<int:comment_id>')
def reply_comment(comment_id):
    comment = Comment.query.get_or_404(comment_id)
    comment_page = request.args.get('page', 1, type = int)
    if not comment.post.can_comment:
        flash('Comment is disabled.', 'warning')
        return redirect(url_for('blog.show_post', post_id = comment.post.id, page= comment_page))
    return redirect(url_for('blog.show_post', post_id=comment.post_id, reply=comment_id, author=comment.author,  page= comment_page) + '#comment-form')


@blog_bp.route('/change-theme/<theme_name>')
def change_theme(theme_name):
    if theme_name not in current_app.config['BLUEBLOG_THEMES'].keys():
        abort(404)
    response = make_response(redirect_back())
    response.set_cookie('theme', theme_name, max_age=30*24*60*60)  # 将cookie的过期时间设 为30天。
    return response

