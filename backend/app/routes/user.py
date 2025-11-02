from flask import Blueprint, request, jsonify, current_app
from app.models.user import User
from app.utils.helpers import save_users_to_json, generate_guid, hash_password, validate_username, validate_password, check_started_game_exists_for_user
from app.schemas.crossword_schema import CrosswordSchema
from app.schemas.game_schema import GameSchema

user_bp = Blueprint('user', __name__)

@user_bp.route('/login', methods=['POST'])
def login():
    # Handling user login
    try:
        # Retrieve JSON payload from request body
        data = request.get_json()
        # Extract username and password
        username = data.get('username', None)
        password = data.get('password', None)

        # Validate presence of username and password
        if not username or not password:
            return jsonify({
                'result': 'failure',
                'message': 'Username and password are required',
                'error': 'Missing credentials'
            }), 400
        else:
            # Check against loaded users in app config
            for id, user in current_app.config['USERS'].items():
                # Validate username and password
                if user.username == username and user.password == hash_password(password):
                    # Let's fetch a security token for the session
                    security_token = user.security_token

                    # Let's check if there is a game in progress for this user so we can return it back to frontend
                    game = check_started_game_exists_for_user(id)

                    return jsonify({
                        'result': 'success',
                        'message': 'Login successful',
                        'user_id': id,
                        'username': user.username,
                        'security_token': security_token,
                        'crossword': CrosswordSchema.dump(game.get_crossword()) if game else None,
                        'game_state': GameSchema.dump_state(game) if game else None
                    }), 200

            # If no match found, return invalid credentials response
            return jsonify({
                'result': 'failure',
                'message': 'Invalid credentials supplied',
                'error': 'Invalid credentials'
            }), 401
    except Exception as e:
        return jsonify({
            'result': 'failure',
            'message': 'Error during login',
            'error': str(e)
        }), 500

@user_bp.route('/register', methods=['POST'])
def register():
    # Handling user registration
    try:
        # Retrieve JSON payload from request body
        data = request.get_json()
        # Extract username and password
        username = data.get('username', None)
        password = data.get('password', None)
        email = data.get('email', None)

        # Validate presence of username and password
        if not username or not password:
            return jsonify({
                'result': 'failure',
                'message': 'Username and password are required to register new user',
                'error': 'Missing username or password'
            }), 400
        elif not validate_username(username):
            return jsonify({
                'result': 'failure',
                'message': 'Invalid username format',
                'error': 'Username must be at least 3 characters long'
            }), 400
        elif not validate_password(password):
            return jsonify({
                'result': 'failure',
                'message': 'Invalid password format',
                'error': 'Password must be at least 6 characters long'
            }), 400
        else:
            # Check against loaded users in app config if a username with the same name exists
            for id, user in current_app.config['USERS'].items():
                if user.username == username:
                    return jsonify({
                        'result': 'failure',
                        'message': 'Username already exists, please choose a different one',
                        'error': 'Username already exists'
                    }), 401

            # If no match found, let's register the new user
            current_app.config['LAST_USER_ID'] += 1
            id = current_app.config['LAST_USER_ID']

            # Let's generate a security token for the session
            security_token = generate_guid()

            new_user = User(
                    user_id=id,
                    username=username,
                    password=hash_password(password),
                    security_token=security_token,
                    email=email
            )
            # Add new user to app config
            current_app.config['USERS'][id] = new_user

            # We need to persist the new user to the users.json file
            save_users_to_json()

            # Return success response back to frontend
            return jsonify({
                'result': 'success',
                'message': 'User registered successfully',
                'user_id': id,
                'username': username,
                'security_token': security_token
            }), 200
    except Exception as e:
        return jsonify({
            'result': 'failure',
            'message': 'Error during new user registration',
            'error': str(e)
        }), 500

