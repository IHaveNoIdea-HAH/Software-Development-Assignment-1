import json
import os
from flask import current_app
from app.schemas.user_schema import UserSchema

def load_json(path, filename):
    """Loads data from JSON """
    try:
        with open(os.path.join(path, filename), 'r') as f:
            data = json.load(f)
        print(f"Data has been loaded from JSON.")
    except Exception as e:
        print(f"Error loading JSON file: {e}")
        data = None

    return data

def save_json(path, filename, data):
    """Saves data to JSON """
    try:
        with open(os.path.join(path, filename), 'w') as f:
            json.dump(data, f, indent=4)
        print(f"Data has been saved to JSON.")
    except Exception as e:
        print(f"Error saving JSON file: {e}")

def validate_username(username):
    """Validates username format"""
    if not username or len(username) < 3:
        return False
    return True

def validate_password(password):
    """Validates password format"""
    if not password or len(password) < 6:
        return False
    return True

def validate_email(email):
    """Validates email format"""
    if not email or "@" not in email:
        return False
    return True

def save_users_to_json():
    """Saves users dictionary to JSON file"""
    try:
        # Convert users dictionary to list for serialization
        users_list = [UserSchema.dump(user) for user in current_app.config['USERS'].values()]
        with open(os.path.join(current_app.config['DATA_FOLDER_PATH'], 'users.json'), 'w') as f:
            json.dump(users_list, f, indent=4)
        print(f"Users data has been saved to JSON.")
    except Exception as e:
        print(f"Error saving users to JSON file: {e}")
