## How to run it
0) build virtual env with python 3.7; pip install -r requirements.txt
1) run run.py to run flask
2) run model.py to build a database, add data into database
## Folder structure
- app
    - auth
        - __init__.py: init auth blueprint
        - forms.py: set form 
        - views.py: set route for auth
    - __init__.py: init flask app; init login manager and set load_user function; init db; set create_app with imported auth blueprint
    - models.py: import db from __init__.py, set db and add data into db
- app.db (build by model.py)
- config.py
- run.py: run create_app with setting from config
![image](https://user-images.githubusercontent.com/83570482/154403451-668a375d-cd2a-485b-879e-cca67a48f72f.png)

Video recommandation: https://www.bilibili.com/video/BV1Jz4y1m7iv?from=search&seid=14798155180876883577&spm_id_from=333.337.0.0

## Final web app


https://user-images.githubusercontent.com/83570482/154403201-78ecde4c-3f47-4111-bbd5-0910ae8174a2.mp4

