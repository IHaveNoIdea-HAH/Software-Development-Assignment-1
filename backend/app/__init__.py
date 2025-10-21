from flask import Flask
from .routes.game import game_bp
from .routes.user import user_bp
from .utils.helpers import load_json
from .schemas.user_schema import UserSchema
import os

def create_app(current_folder):
    app = Flask("crossword_backend")
    app.config.from_object('app.config.Config')

    # Define path to the data folder
    data_folder = os.path.join(current_folder, 'app', 'data')
    app.config['DATA_FOLDER_PATH'] = data_folder

    # Let's load data for crosswords generation into app config
    print('Loading crossword data from JSON...')
    app.config['CROSSWORDS_DATA'] = load_json(data_folder, 'crossword_words.json')

    # Let's load info about users of our crossword game into app config
    print('Loading users data from JSON...')
    users = load_json(data_folder, 'users.json')
    # Convert list of users into a dictionary for easy access
    # and also deserialize using UserSchema
    for user in users:
        app.config['USERS'][user['id']] = UserSchema.load(user)

    # Set the LAST_USER_ID based on loaded users
    app.config['LAST_USER_ID'] = len(app.config['USERS'])

    # Register blueprints for different routes
    # This will expose them under /api/game and /api/user to frontend app calls
    print('Registering blueprints...')
    app.register_blueprint(game_bp, url_prefix='/api/game')
    app.register_blueprint(user_bp, url_prefix='/api/user')
    print('Blueprints registered.')
    print('Flask app setup complete.')
    return app

