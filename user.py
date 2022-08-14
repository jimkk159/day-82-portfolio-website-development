from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user
# encryption
from werkzeug.security import generate_password_hash, check_password_hash

# self import
from extension import db
from forms import LoginForm, RegisterForm
from SQL.SQL_management import User

user_blueprint = Blueprint('user', __name__)


# Login
@user_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        query_user = User.query.filter_by(email=login_form.email.data).first()

        # check user exist
        if not query_user:
            flash('User not exists')
            return redirect(url_for('user.login'))

        # check password
        if check_password_hash(query_user.password, login_form.password.data):
            login_user(query_user)

            return redirect(url_for('home'))
        else:
            flash('Password wrong')
            return redirect(url_for('user.login'))

    return render_template('login.html', login_form=login_form)


# Register
@user_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    register_form = RegisterForm()
    if register_form.validate_on_submit():

        # confirm password
        if register_form.password.data != register_form.password_confirm.data:
            flash('Confirm password fail')
            return redirect(url_for('user.register'))

        # repeat register
        if User.query.filter_by(email=register_form.email.data).first():
            flash('Email already exists')
            return redirect(url_for('user.login'))

        new_user = User(email=register_form.email.data,
                        name=register_form.name.data,
                        password=generate_password_hash(register_form.password.data, method='pbkdf2:sha256',
                                                        salt_length=8))
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('register.html', register_form=register_form)
