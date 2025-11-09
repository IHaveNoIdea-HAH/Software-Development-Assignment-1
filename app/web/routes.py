from flask import Blueprint, render_template
import os

web_bp = Blueprint('web', __name__)

@web_bp.route('/')
def home():
    # Render the homepage template which has the game rules and includes links to register, login and play pages
    api_base = os.environ.get('API_BASE_URL', '')
    return render_template('homepage.html', api_base=api_base)

@web_bp.route('/play')
def play():
    # Render the main game interface template
    api_base = os.environ.get('API_BASE_URL', '')
    return render_template('play.html', api_base=api_base)

@web_bp.route('/login')
def login_page():
    # Render the login page template
    api_base = os.environ.get('API_BASE_URL', '')
    return render_template('login.html', api_base=api_base)

@web_bp.route('/register')
def register_page():
    # Render the registration page template
    api_base = os.environ.get('API_BASE_URL', '')
    return render_template('register.html', api_base=api_base)

@web_bp.route('/rest_api_test')
def rest_api_test():
    # Render a simple page to test REST API connectivity
    api_base = os.environ.get('API_BASE_URL', '')
    return render_template('rest_api_test.html', api_base=api_base)
