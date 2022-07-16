from . import db, bcrypt
from . import login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)
    phone_number = db.Column(db.String(32), nullable=False)
    item = db.Column(db.String(32), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('customers', lazy=True))

    def __repr__(self):
        return f'Customer {self.name}'


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    @property
    def password(self):
        return self.password_hash

    @password.setter
    def password(self, password_to_hash):
        self.password_hash = bcrypt.generate_password_hash(password_to_hash).decode('utf-8')

    def check_password(self, password_to_check):
        return bcrypt.check_password_hash(self.password_hash, password_to_check)