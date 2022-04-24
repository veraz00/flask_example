## How to run it 
python -m flask run   == python manager.py
python -m flask db init
python -m flask db migrate -m "Admin" 
python -m flask db upgrade
python -m flask init   # call funtion 
python -m flask forge 

## Directory structure 
sayhello
│  app.db
│  config.py
│  manager.py
│  Readme.md
│
├─app
│  │  extensions.py
│  │  faker.py
│  │  forms.py
│  │  models.py
│  │  utils.py
│  │  __init__.py
│  │
│  ├─static
│  │  │  favicon.ico
│  │  │  icons8-puzzle-48.ico
│  │  ├─css
│  │  └─js
│  │
│  ├─templates
│  │  │  base.html
│  │  └─sayhello - message.html
│  │
│  ├─views
│    └─sayhello
│        views.py
│         __init__.py
│
└─migrations


## Need to improve
How to put error message in form??