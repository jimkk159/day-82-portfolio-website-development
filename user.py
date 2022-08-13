from flask import Blueprint, render_template
from forms import LoginForm, RegisterForm

user_blueprint = Blueprint('user', __name__)


# Login
@user_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        print(login_form.email.data, login_form.password.data)
    return render_template('login.html', login_form=login_form)


# Register
@user_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    register_form = RegisterForm()
    if register_form.validate_on_submit():
        print(register_form.email.data, register_form.name.data, register_form.password.data,
              register_form.password_confirm.data)
    return render_template('register.html', register_form=register_form)
