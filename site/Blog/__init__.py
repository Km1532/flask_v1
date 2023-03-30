from flask import Flask
from Flask_bcrypt import Bcrypt
from Flask_login import LoginManager
from Flask_sqlalcnemy import SQLAlchemy

db = SQLAlchemy()
bcrypt = Bcrypt


login_manager = LoginManager()
login_manager.login_view = 'main.login'
login_manager.login_message_category = 'info'

def create_app():
app = Flask(__name__)
    app.config.from_pyfile('main/settings.py')
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

from blog.main.routes import main

 app.register_blueprint(main)

return app

app_ctx = create_app()

def create_user():
    with app_ctx.app_context():
        from blog.models import User
        
        db.drop_all()
        db.create_all()
        hashed_password = bcrypt.generate_password_hash('12345').decode('uft-8')
        user = User(username='Mike', email='mike_admin@blog.com', password=hashed_password)
        db.session.add(user)
        db.session.commit()