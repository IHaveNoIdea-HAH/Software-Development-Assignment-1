import requests
import random
import string

# Set to True to print debug data
print_debug_data = False

def test_game_start_post():
    print("Testing game start POST endpoint and successful outcome...")
    url = "http://localhost:5000/api/game/start"
    payload = {
        "gameDifficultyLevel": "normal",
        "userId": 1
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(url, json=payload, headers=headers)
    assert response.status_code == 200
    data = response.json()
    if print_debug_data:
        print(data)
    assert "game_id" in data
    assert "crossword" in data
    assert "result" in data
    assert data["result"] == "success"
    assert data["message"] == "Game started"

def test_game_start_post_unknown_user():
    print("Testing game start POST endpoint with unknown user...")
    url = "http://localhost:5000/api/game/start"
    payload = {
        "gameDifficultyLevel": "normal",
        "userId": 9999  # Assuming this user ID does not exist
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(url, json=payload, headers=headers)
    assert response.status_code == 400
    data = response.json()
    if print_debug_data:
        print(data)
    assert "result" in data
    assert data["result"] == "failure"
    assert data["message"] == "Unknown user. Please log in to start a game."


def test_login_post_invalid_credentials():
    print("Testing user login POST endpoint with invalid credentials...")
    url = "http://localhost:5000/api/user/login"
    payload = {
        "username": "invalid_user",
        "password": "wrong_password"
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(url, json=payload, headers=headers)
    assert response.status_code == 401
    data = response.json()
    if print_debug_data:
        print(data)
    assert "result" in data
    assert data["result"] == "failure"
    assert data["message"] == "Invalid credentials supplied"


def test_login_post_missing_credentials():
    print("Testing user login POST endpoint with missing credentials...")
    url = "http://localhost:5000/api/user/login"
    payload = {
        "username": "",
        "password": ""
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(url, json=payload, headers=headers)
    assert response.status_code == 400
    data = response.json()
    if print_debug_data:
        print(data)
    assert "result" in data
    assert data["result"] == "failure"
    assert data["message"] == "Username and password are required"


def test_login_post_success():
    print("Testing user login POST endpoint with valid credentials...")
    url = "http://localhost:5000/api/user/login"
    payload = {
        "username": "testuser",
        "password": "testpassword"
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(url, json=payload, headers=headers)
    assert response.status_code == 200
    data = response.json()
    if print_debug_data:
        print(data)
    assert "result" in data
    assert data["result"] == "success"
    assert data["message"] == "Login successful"
    assert "user_id" in data
    assert "username" in data

def test_register_new_user_post_success():
    print("Testing user registration POST endpoint with valid data...")
    url = "http://localhost:5000/api/user/register"

    def generate_random_string(length=6):
        """Generates a random string of uppercase letters with the specified length."""
        return ''.join(random.choices(string.ascii_uppercase, k=length))

    payload = {
        "username": generate_random_string(length=6),
        "password": generate_random_string(length=6),
        "email": "newuser@gmail.com"
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(url, json=payload, headers=headers)
    assert response.status_code == 200
    data = response.json()
    if print_debug_data:
        print(data)
    assert "result" in data
    assert data["result"] == "success"
    assert data["message"] == "User registered successfully"
    assert "user_id" in data
    assert "username" in data

def test_register_new_user_post_missing_username():
    print("Testing user registration POST endpoint with missing username...")
    url = "http://localhost:5000/api/user/register"

    payload = {
        "password": "validpassword",
        "email": "new@mail.com"
    }

    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(url, json=payload, headers=headers)
    assert response.status_code == 400
    data = response.json()
    if print_debug_data:
        print(data)
    assert "result" in data
    assert data["result"] == "failure"
    assert data["message"] == "Username and password are required to register new user"
    assert "error" in data
    assert data["error"] == "Missing username or password"

def test_register_new_user_post_user_exists():
    print("Testing user registration POST endpoint with existing username...")
    url = "http://localhost:5000/api/user/register"

    payload = {
        "username": "testuser",  # Assuming this username already exists
        "password": "testpassword",
        "email": "email@mail.com"
    }

    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(url, json=payload, headers=headers)
    assert response.status_code == 401
    data = response.json()
    if print_debug_data:
        print(data)

    assert "result" in data
    assert data["result"] == "failure"
    assert data["message"] == "Username already exists, please choose a different one"
    assert "error" in data
    assert data["error"] == "Username already exists"

if __name__ == "__main__":
    # Run the tests
    # Testing game start with valid user
    test_game_start_post()
    # Testing game start with unknown user
    test_game_start_post_unknown_user()
    # Testing login with invalid credentials
    test_login_post_invalid_credentials()
    # Testing login with missing credentials
    test_login_post_missing_credentials()
    # Testing login with valid credentials
    test_login_post_success()
    # Testing user registration with valid data
    test_register_new_user_post_success()
    # Validate presence of username and password
    test_register_new_user_post_missing_username()
    # Validate existing username
    test_register_new_user_post_user_exists()