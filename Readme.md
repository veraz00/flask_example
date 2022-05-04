# Flask Blog

## Original resource
- Demo: http://bluelog.helloflask.com/
- Code preference: https://github.com/greyli/bluelog

## Command 

```
python -m flask run   == python manager.py
# Flask会自动从环境变量FLASK_APP的值定义的模块 中寻找名为create_app（); 目前程序中的db.create_all（）方法可以被正确执行

python -m flask db init
python -m flask db migrate -m "Admin" 
python -m flask db upgrade
python -m flask init   # call funtion 
python -m flask forge 
flask routes # check all routes 
```
