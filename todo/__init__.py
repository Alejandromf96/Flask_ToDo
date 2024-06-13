import os 
from . import db
from flask import Flask
from . import auth
from . import todo
from dotenv import load_dotenv

def create_app():
    load_dotenv()
    app = Flask(__name__)

    app.config.from_mapping(
        SECRET_KEY='mikey',
        DATABASE_HOST=os.environ.get('FLASK_DATABASE_HOST'),
        DATABASE_PASSWORD=os.environ.get('FLASK_DATABASE_PASSWORD'),
        DATABASE_USER=os.environ.get('FLASK_DATABASE_USER'),
        DATABASE=os.environ.get('FLASK_DATABASE'),
    )

    
    db.init_app(app)

    app.register_blueprint(auth.bp)
    app.register_blueprint(todo.bp)

    @app.route('/hola')
    def hola():
        return 'Hola'

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)