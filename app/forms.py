from os import name
from flask.app import Flask
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, DateField, SelectField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, URL


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=8, message="A username should not be less than 8 characters")])
    password = PasswordField('Password', validators=[DataRequired(message="Please enter a password"), 
                                                     Length(min=8, message="Password must be at least 8 characters long.")])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
    
class StoreForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    address = TextAreaField('Address')
    phone = StringField('Phone')
    active = BooleanField('Active')
    duplicate = SubmitField('Duplicate')
    add_new = SubmitField('Add New')
    submit = SubmitField('Submit')
    update = SubmitField('Update')

class UserForm(FlaskForm):
    first_name = StringField('First name', validators=[DataRequired(message="Enter a First Name")])
    last_name = StringField('Last name(s)', validators=[DataRequired(message="Enter the last name(s) of the user")])
    phone = StringField('Phone')
    address = TextAreaField('Address')
    username = StringField('Username')
    password = PasswordField('Password')
    repeat_password = PasswordField('Repeat Password')
    email = StringField('Email')
    role = SelectField('Role')
    store = SelectField('Store')
    active = BooleanField('Active')
    duplicate = SubmitField('Duplicate')
    add_new = SubmitField('Add New')
    submit = SubmitField('Submit')
    update = SubmitField('Update')
    

class ProductForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    availability = SelectField('Availability')
    sales_price = IntegerField('Sales Price')
    low_level = IntegerField('Low level')
    active = BooleanField('Active')
    duplicate = SubmitField('Duplicate')
    add_new = SubmitField('Add New')
    submit = SubmitField('Submit')
    update = SubmitField('Update')

class PurchaseForm(FlaskForm):
    date = DateField('Date',  validators=[DataRequired(message="Pick a date")])
    supplier_name = SelectField('Supplier name', validators=[DataRequired(message="Pick a Supplier or create a new one")])
    product_name = SelectField('Product Name', validators=[DataRequired(message="Select a product")])
    driver_name = StringField('Driver\'s Name')
    driver_phone = StringField('Driver\'s Phone No.')
    vehicle_no = StringField('Vehicle No.')
    quantity = IntegerField('Quantity')
    cost_price = IntegerField('Sales Price')
    trans_cost = IntegerField('Transport Cost')
    store_name = SelectField('Store Name')
    duplicate = SubmitField('Duplicate')
    add_new = SubmitField('Add New')
    submit = SubmitField('Submit')
    update = SubmitField('Update')

class SalesForm(FlaskForm):
    date = DateField('Date',  validators=[DataRequired(message="Pick a date")])
    customer_name = SelectField('Customer Name', validators=[DataRequired(message="Pick a Customer or create a new one")])
    product_name = SelectField('Product Name', validators=[DataRequired(message="Select a product")])
    quantity = IntegerField('Quantity')
    unit_price = IntegerField('Unit Price')
    discount = IntegerField('Discount')
    store_name = SelectField('Store Name')
    duplicate = SubmitField('Duplicate')
    add_new = SubmitField('Add New')
    submit = SubmitField('Submit')
    update = SubmitField('Update')
    
class UserRolesForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    privileges = SelectField('Privileges')
    active = BooleanField('Active')
    duplicate = SubmitField('Duplicate')
    add_new = SubmitField('Add New')
    submit = SubmitField('Submit')
    update = SubmitField('Update')

class SettingsForm(FlaskForm):
    company_name = StringField('Company Name', validators=[DataRequired()])
    address = TextAreaField('Address')
    phone = StringField('Phone')
    email = StringField('Email')
    website = StringField('Website')
    logo = SubmitField('Upload')
    update = SubmitField('Update')