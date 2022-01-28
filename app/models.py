from datetime import datetime
from enum import unique
from app import db
#credentials for hashing a password
from werkzeug.security import generate_password_hash, check_password_hash

#credentials for logging in a user
from flask_login import UserMixin
from app import login


#credentials for logging in a user
@login.user_loader
def load_user(id):
    return User.query.get(int(id))


user_roles = db.Table('user_roles',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('role_id', db.Integer, db.ForeignKey('role.id'), primary_key=True)
)
    
    
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(128), index=True, nullable=False)
    last_name = db.Column(db.String(128), index=True, nullable=False)
    phone = db.Column(db.String(20))
    address = db.Column(db.String(256))
    username = db.Column(db.String(128))
    password_hash = db.Column(db.String(180))
    email = db.Column(db.String(180))
    roles = db.relationship('Role', secondary=user_roles, backref='user', lazy='dynamic')
    store_id = db.Column(db.Integer, db.ForeignKey('store.id'))
    active = db.Column(db.Boolean, index=True)
    sales = db.relationship('Sale', backref='user', lazy='dynamic')
    purchases = db.relationship('Purchase', backref='user', lazy='dynamic')

    def __repr__(self):
        return '<User {} {}>'.format(self.first_name, self.last_name)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    

class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), index=True, nullable=False)
    privileges = db.Column(db.Integer, nullable=False)
    active = db.Column(db.Boolean, index=True)

    def __repr__(self):
        return '<Role {}>'.format(self.name)


class Store(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), index=True, unique=True, nullable=False)
    address = db.Column(db.String(256))
    phone = db.Column(db.String(20))
    active = db.Column(db.Boolean, index=True)
    users = db.relationship('User', backref='store', lazy='dynamic')
    products = db.relationship('Product', backref='store', lazy='dynamic')
    purchases = db.relationship('Purchase', backref='store', lazy='dynamic')
    sales = db.relationship('Sale', backref='store', lazy='dynamic')

    def __repr__(self):
        return '<Store {}>'.format(self.name)

    
class Sale(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    customer_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Float)
    unit_price = db.Column(db.Float)
    discount = db.Column(db.Float)
    store_id = db.Column(db.Integer, db.ForeignKey('store.id'), nullable=False)

    def __repr__(self):
        return '<Sales id {}>'.format(self.id)

    
class Purchase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    supplier_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    driver_name = db.Column(db.String(128))
    driver_phone = db.Column(db.String(20))
    vehicle_no = db.Column(db.String(20))
    quantity = db.Column(db.Float)
    cost_price = db.Column(db.Float)
    transport_cost = db.Column(db.Float)
    store_id = db.Column(db.Integer, db.ForeignKey('store.id'), nullable=False)

    def __repr__(self):
        return '<Purchase id {}>'.format(self.id)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    description = db.Column(db.String(256))
    store_id = db.Column(db.Integer, db.ForeignKey('store.id'), nullable=False)
    sales_price = db.Column(db.Float)
    low_level = db.Column(db.Float)
    active = db.Column(db.Boolean, index=True)
    sales = db.relationship('Sale', backref='product', lazy='dynamic')
    purchases = db.relationship('Purchase', backref='product', lazy='dynamic')

    def __repr__(self):
        return '<Product name: {}>'.format(self.name)


class Setting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(180), index=True, nullable=False)
    address = db.Column(db.String(256))
    phone = db.Column(db.String(20))
    email = db.Column(db.String(180))
    website = db.Column(db.String(180))
    logo = db.Column(db.String(250))

    def __repr__(self):
        return '<Main Settings of: {}>'.format(self.company_name)
    
