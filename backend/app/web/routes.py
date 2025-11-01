from flask import Blueprint, render_template

web_bp = Blueprint('web', __name__)

@web_bp.route('/')
def home():
    # Render the homepage template which has the game rules and includes links to register, login and play pages
    return render_template('homepage.html')

@web_bp.route('/play')
def play():
    # Render the main game interface template
    return render_template('play.html')

@web_bp.route('/login')
def login_page():
    # Render the login page template
    return render_template('login.html')

@web_bp.route('/register')
def register_page():
    # Render the registration page template
    return render_template('register.html')

@web_bp.route('/rest_api_test')
def rest_api_test():
    # Render a simple page to test REST API connectivity
    return render_template('rest_api_test.html')
