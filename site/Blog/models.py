from flask_bcrypt import check_password_hash, generate_password_hash
from flask_login import UserMixin
from blog import db, login_manager, bcrypt

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    __tablename__ = "user"

    id = db.Column(db_Interger, primary_key=True)
    username = db.Column(db.String(20), uniqe=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable = Flase)
    password = db.Column(db.String(60), nullable=False)

    def set_password(self,password, hashed_password):
        self.hashed_password = bcrypt.generate_password_hash(password).decode('uft-8')

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)

    def __repr__(self):
        return f'User({self.username}, {self.email}, {self.password}'