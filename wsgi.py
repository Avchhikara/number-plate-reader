from os import getenv
from app import app

if __name__ == "__main__":
    app.secret_key = getenv('FLASK_SECRET_KEY') or "TEMP_SECRET_KEY"
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run()
