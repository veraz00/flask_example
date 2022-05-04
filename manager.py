
from app import create_app
if __name__ == '__main__':
    app = create_app('development')
    app.run(host = '192.168.1.13', port = 8000, debug=True)
