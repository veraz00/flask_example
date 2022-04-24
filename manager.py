
from app import create_app
if __name__ == '__main__':
    app = create_app('develop')
    app.run(host = '0.0.0.0', port = 8000, debug=True)


# echo "# Flask_example" >> README.md
# git init
# git add README.md
# git commit -m "first commit"
# git branch -M main
# git remote add origin https://github.com/veraz00/Flask_example.git
# git push -u origin main
# …or push an existing repository from the command line
# git remote add origin https://github.com/veraz00/Flask_example.git
# git branch -M main
# git push -u origin main