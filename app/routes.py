from flask import render_template, flash, redirect, url_for, make_response
from flask_login.utils import logout_user
from app import app
from app.forms import LoginForm, SalesForm, StoreForm, UserForm, ProductForm, PurchaseForm, UserRolesForm, SettingsForm

#credentials for logging in a user
from flask_login import current_user, login_user
from app.models import User
from flask_login import login_required

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
        
    return render_template('login.html', title='Sign In', form=form)


@app.route('/')
@app.route('/dashboard')
@login_required
def index():
    user = {'username': 'memorila', 'password': 'iloveyou'}
    
    return render_template('index.html', title='Dashboard', user = user)


@app.route('/stores', methods=['GET', 'POST'])
def stores():
    form = StoreForm()
    
    if form.add_new():
        return render_template('stores.html', title='Add Store', header ="Add Store", form=form)
    
    if form.validate_on_submit():
        
        flash('Store {} has been added successfully.'.format(
            form.name.data))
        return render_template('stores.html', title='Update Store', header='Update Store', form=form)
    return render_template('stores.html', title='Add Store', header ="Add Store", form=form)


@app.route('/users', methods=['GET', 'POST'])
def users():
    form = UserForm()
    
    return render_template('users.html', title='Add User', header="Add User", form=form)
    

@app.route('/suppliers', methods=['GET', 'POST'])
def suppliers():
    form = UserForm()
    
    return render_template('suppliers.html', title='Add Supplier', header='Add Supplier', form=form)

@app.route('/customers', methods=['GET', 'POST'])
def customers():
    
    form = UserForm()
    
    return render_template('customers.html', title='Add Customer', header='Add Customer', form=form)

@app.route('/products', methods=['GET', 'POST'])
def products():
    form = ProductForm()
    
    return render_template('products.html', title='Add Product', header='Add Product', form=form)

@app.route('/purchases', methods=['GET', 'POST'])
def purchases():
    form = PurchaseForm()
    return render_template('purchases.html', title='Make Purchase', header='Make Purchase', form=form)

@app.route('/sales', methods=['GET', 'POST'])
def sales():
    form = SalesForm()
    return render_template('sales.html', title='Make Sales', header='Make Sales', form=form)


@app.route('/settings', methods=['GET', 'POST'])
def settings():
    form = SettingsForm()
    return render_template('settings.html', title='Main Settings', header='Main Settings', form=form)


@app.route('/user-roles', methods=['GET', 'POST'])
def user_roles():
    form = UserRolesForm()
    return render_template('user-roles.html', title='Add User Role', header='Add User Role', form=form)

@app.route('/reports', methods=['GET', 'POST'])
def reports():
    return render_template('reports.html', title='Reports')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.errorhandler(404)
def not_found():
    """Page not found."""
    return make_response(
        render_template("404.html"),
        404
     )


@app.errorhandler(400)
def bad_request():
    """Bad request."""
    return make_response(
        render_template("400.html"),
        400
    )


@app.errorhandler(500)
def server_error():
    """Internal server error."""
    return make_response(
        render_template("500.html"),
        500
    )
