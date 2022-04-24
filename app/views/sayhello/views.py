from re import M
from flask import render_template, url_for, redirect , request, current_app, flash, session

from app.views.sayhello import sayhello
from app.models import Message 
from app.forms import PostForm
from app.extensions import db 

@sayhello.route('/home', methods = ['GET', 'POST'])
def create_post():
    page = request.args.get('page', 2, type=int)

    pagination = Message.query.order_by(Message.timestamp.desc()).paginate(
    page, per_page = current_app.config['PER_PAGE'])
    
    error = None
    form = PostForm()
    if form.validate_on_submit():
        name = form.author.data
        message = form.message.data
        天王盖地虎 = form.天王盖地虎.data

        if 天王盖地虎 != '宝塔镇河妖':
            error = 'The captcha value must be "宝塔镇河妖"'

        
        else:
            mm = Message(name = name, message=message)

            db.session.add(mm)
            db.session.commit()
            flash('Message has been created!', 'success')

            return redirect(url_for('sayhello.create_post'))
    
        
    return render_template('sayhello/message.html', error=error, \
        pagination=pagination.items, form = form, message = pagination)

# in html: for is used for message.items; message.total (message is from sql filter)
