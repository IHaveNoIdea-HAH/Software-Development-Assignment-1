import requests
import random
import string

# Set to True to print debug data
print_debug_data = False

def test_game_start_post():
    print("Testing game start POST endpoint and successful outcome...")
    url = "http://localhost:5000/api/game/start"
    payload = {
        "game_difficulty_level": "normal",
        "user_id": 1,
        "security_token": "41c8fd33-f2c5-4406-a781-15328aa9dfb3"
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(url, json=payload, headers=headers)
    assert response.status_code == 200
    data = response.json()
    if print_debug_data:
        print(data)
    assert "game_state" in data
    assert "crossword" in data
    assert "grid" in data["crossword"]
    assert "clues" in data["crossword"]
    assert "game_id" in data["game_state"]
    assert "user_id" in data
    assert "result" in data
    assert "message" in data
    assert data["result"] == "success"
    assert data["message"] == "Game started"

def test_game_start_post_unknown_user():
    print("Testing game start POST endpoint with unknown user...")
    url = "http://localhost:5000/api/game/start"
    payload = {
        "game_difficulty_level": "normal",
        "user_id": 9999,  # Assuming this user ID does not exist
        "security_token": ""
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


def test_game_start_post_invalid_token():
    print("Testing game start POST endpoint with invalid security token...")
    url = "http://localhost:5000/api/game/start"
    payload = {
        "game_difficulty_level": "normal",
        "user_id": 1,
        "security_token": "wrong_token"
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(url, json=payload, headers=headers)
    assert response.status_code == 403
    data = response.json()
    if print_debug_data:
        print(data)
    assert "result" in data
    assert "message" in data
    assert "error" in data
    assert data["result"] == "failure"
    assert data["message"] == "Invalid security token. Please log in again."
    assert data["error"] == "Security token does not match."


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
    assert "security_token" in data

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
    assert "security_token" in data

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

def test_register_new_user_post_incorrect_username():
    print("Testing user registration POST endpoint with incorrect username format...")
    url = "http://localhost:5000/api/user/register"

    payload = {
        "username": "ab",  # Invalid username (too short)
        "password": "validpassword",
        "email": "",
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
    assert data["message"] == "Invalid username format"
    assert "error" in data
    assert data["error"] == "Username must be at least 3 characters long"

def test_register_new_user_post_incorrect_password():
    print("Testing user registration POST endpoint with incorrect password format...")
    url = "http://localhost:5000/api/user/register"

    payload = {
        "username": "newuser",
        "password": "123",  # Invalid password (too short)
        "email": "",
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
    assert data["message"] == "Invalid password format"
    assert "error" in data
    assert data["error"] == "Password must be at least 6 characters long"

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

def test_game_guess_word_post_invalid_security_token():
    print("Testing game guess word POST endpoint with invalid security token...")
    url = "http://localhost:5000/api/game/guess_word"
    payload = {
        "clue_number": 1,
        "game_id": 1,
        "user_id": 1,
        "security_token": "invalid_token",
        "word_guess": "TESTWORD"
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(url, json=payload, headers=headers)
    assert response.status_code == 403
    data = response.json()
    if print_debug_data:
        print(data)
    assert "result" in data
    assert data["result"] == "failure"
    assert "message" in data
    assert data["message"] == "Invalid security token. Please log in again."
    assert "error" in data
    assert data["error"] == "Security token does not match."

def test_game_guess_word_post_invalid_game_id():
    print("Testing game guess word POST endpoint with invalid game ID...")
    url = "http://localhost:5000/api/game/guess_word"
    payload = {
        "clue_number": 1,
        "game_id": 9999,  # Assuming this game ID does not exist
        "user_id": 1,
        "security_token": "41c8fd33-f2c5-4406-a781-15328aa9dfb3",
        "word_guess": "TESTWORD"
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(url, json=payload, headers=headers)
    assert response.status_code == 405
    data = response.json()
    if print_debug_data:
        print(data)
    assert "result" in data
    assert data["result"] == "failure"
    assert data["message"] == "Invalid game id. Please send valid game_id value."
    assert "error" in data
    assert data["error"] == "Game id value does not exist."

def test_game_guess_word_post_missing_clue_number():
    print("Testing game guess word POST endpoint with missing clue number...")
    url = "http://localhost:5000/api/game/guess_word"
    payload = {
        # "clue_number": 1,  # Missing clue number
        "game_id": 1,
        "user_id": 1,
        "security_token": "41c8fd33-f2c5-4406-a781-15328aa9dfb3",
        "word_guess": "TESTWORD"
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
    assert data["message"] == "clue_number is required."
    assert "error" in data
    assert data["error"] == "Missing clue_number."

def test_game_guess_word_post_missing_guess_word():
    print("Testing game guess word POST endpoint with missing guess word...")
    url = "http://localhost:5000/api/game/guess_word"
    payload = {
        "clue_number": 1,
        "game_id": 1,
        "user_id": 1,
        "security_token": "41c8fd33-f2c5-4406-a781-15328aa9dfb3",
        # "word_guess": "TESTWORD"  # Missing word guess
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
    assert data["message"] == "word_guess is required."
    assert "error" in data
    assert data["error"] == "Missing word_guess."

def test_game_guess_word_post_invalid_user():
    print("Testing game guess word POST endpoint with invalid user...")
    url = "http://localhost:5000/api/game/guess_word"
    payload = {
        "clue_number": 1,
        "game_id": 1,
        "user_id": 9999,  # Assuming this user ID does not exist
        "security_token": "",
        "word_guess": "TESTWORD"
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
    assert "error" in data
    assert data["error"] == "Unknown User ID has been received."

def test_game_guess_word_post_clue_number_already_solved():
    print("Testing game guess word POST endpoint with already solved clue number...")
    url = "http://localhost:5000/api/game/guess_word"
    payload = {
        "clue_number": 10,  # Assuming this clue number has already been solved
        "game_id": 1,
        "user_id": 1,
        "security_token": "41c8fd33-f2c5-4406-a781-15328aa9dfb3",
        "word_guess": "TESTWORD"
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(url, json=payload, headers=headers)
    assert response.status_code == 407
    data = response.json()
    if print_debug_data:
        print(data)
    assert "result" in data
    assert data["result"] == "failure"
    assert data["message"] == "Clue number has already been solved."
    assert "error" in data
    assert data["error"] == "clue_number already solved."



def test_game_guess_word_post_invalid_clue_number():
    print("Testing game guess word POST endpoint with invalid clue number...")
    url = "http://localhost:5000/api/game/guess_word"
    payload = {
        "clue_number": 9999,  # Assuming this clue number does not exist
        "game_id": 1,
        "user_id": 1,
        "security_token": "41c8fd33-f2c5-4406-a781-15328aa9dfb3",
        "word_guess": "TESTWORD"
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(url, json=payload, headers=headers)
    assert response.status_code == 406
    data = response.json()
    if print_debug_data:
        print(data)
    assert "result" in data
    assert data["result"] == "failure"
    assert data["message"] == "Invalid clue number provided."
    assert "error" in data
    assert data["error"] == "clue_number is invalid."


def test_game_solve_clue_post_clue_number_is_already_solved():
    print("Testing game solve clue POST endpoint with already solved clue number...")
    url = "http://localhost:5000/api/game/solve_clue"
    payload = {
        "clue_number": 10,  # Assuming this clue number has already been solved
        "game_id": 1,
        "user_id": 1,
        "security_token": "41c8fd33-f2c5-4406-a781-15328aa9dfb3"
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(url, json=payload, headers=headers)
    assert response.status_code == 407
    data = response.json()
    if print_debug_data:
        print(data)
    assert "result" in data
    assert data["result"] == "failure"
    assert data["message"] == "Clue number has already been solved."
    assert "error" in data
    assert data["error"] == "clue_number already solved."

def test_game_solve_clue_post_clue_number_is_missing():
    print("Testing game solve clue POST endpoint with missing clue number...")
    url = "http://localhost:5000/api/game/solve_clue"
    payload = {
        # "clue_number": 1,  # Missing clue number
        "game_id": 1,
        "user_id": 1,
        "security_token": "41c8fd33-f2c5-4406-a781-15328aa9dfb3"
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
    assert data["message"] == "clue_number is required."
    assert "error" in data
    assert data["error"] == "Missing clue_number."

def test_game_solve_clue_post_invalid_game_id():
    print("Testing game solve clue POST endpoint with invalid game ID...")
    url = "http://localhost:5000/api/game/solve_clue"
    payload = {
        "clue_number": 1,
        "game_id": 9999,  # Assuming this game ID does not exist
        "user_id": 1,
        "security_token": "41c8fd33-f2c5-4406-a781-15328aa9dfb3"
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(url, json=payload, headers=headers)
    assert response.status_code == 405
    data = response.json()
    if print_debug_data:
        print(data)
    assert "result" in data
    assert data["result"] == "failure"
    assert data["message"] == "Invalid game id. Please send valid game_id value."
    assert "error" in data
    assert data["error"] == "Game id value does not exist."

def test_game_solve_clue_post_invalid_security_token():
    print("Testing game solve clue POST endpoint with invalid security token...")
    url = "http://localhost:5000/api/game/solve_clue"
    payload = {
        "clue_number": 1,
        "game_id": 1,
        "user_id": 1,
        "security_token": "invalid_token"
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(url, json=payload, headers=headers)
    assert response.status_code == 403
    data = response.json()
    if print_debug_data:
        print(data)
    assert "result" in data
    assert data["result"] == "failure"
    assert "message" in data
    assert data["message"] == "Invalid security token. Please log in again."
    assert "error" in data
    assert data["error"] == "Security token does not match."


def test_game_solve_clue_post_unknown_user():
    print("Testing game solve clue POST endpoint with unknown user...")
    url = "http://localhost:5000/api/game/solve_clue"
    payload = {
        "clue_number": 1,
        "game_id": 1,
        "user_id": 9999,  # Assuming this user ID does not exist
        "security_token": ""
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
    assert "error" in data
    assert data["error"] == "Unknown User ID has been received."


def test_game_solve_clue_post_invalid_clue_number():
    print("Testing game solve clue POST endpoint with invalid clue number...")
    url = "http://localhost:5000/api/game/solve_clue"
    payload = {
        "clue_number": 9999,  # Assuming this clue number does not exist
        "game_id": 1,
        "user_id": 1,
        "security_token": "41c8fd33-f2c5-4406-a781-15328aa9dfb3"
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(url, json=payload, headers=headers)
    assert response.status_code == 406
    data = response.json()
    if print_debug_data:
        print(data)
    assert "result" in data
    assert data["result"] == "failure"
    assert data["message"] == "Invalid clue number provided."
    assert "error" in data
    assert data["error"] == "clue_number is invalid."


def test_game_auto_solve_post_invalid_security_token():
    print("Testing game auto solve POST endpoint with invalid security token...")
    url = "http://localhost:5000/api/game/auto_solve"
    payload = {
        "game_id": 1,
        "user_id": 1,
        "security_token": "invalid_token"
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(url, json=payload, headers=headers)
    assert response.status_code == 403
    data = response.json()
    if print_debug_data:
        print(data)
    assert "result" in data
    assert data["result"] == "failure"
    assert "message" in data
    assert data["message"] == "Invalid security token. Please log in again."
    assert "error" in data
    assert data["error"] == "Security token does not match."


def test_game_auto_solve_post_invalid_user():
    print("Testing game auto solve POST endpoint with invalid user...")
    url = "http://localhost:5000/api/game/auto_solve"
    payload = {
        "game_id": 1,
        "user_id": 9999,  # Assuming this user ID does not exist
        "security_token": ""
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
    assert "error" in data
    assert data["error"] == "Unknown User ID has been received."

def test_game_guess_word_post_invalid_guess():
    print("Testing game guess word POST endpoint with invalid guess...")
    url = "http://localhost:5000/api/game/guess_word"
    payload = {
        "clue_number": 1,
        "game_id": 1,
        "user_id": 1,
        "security_token": "41c8fd33-f2c5-4406-a781-15328aa9dfb3",
        "word_guess": "WRONGWORD"
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
    assert "message" in data
    assert data["message"] == "Incorrect guess."
    assert "is_correct" in data
    assert data["is_correct"] == False
    assert "answer" in data
    assert "points_scored" in data
    assert data["points_scored"] == 0
    assert "game_state" in data
    assert "crossword" in data
    assert "grid" in data["crossword"]
    assert "clues" in data["crossword"]


def test_game_auto_solve_post_invalid_game_id():
    print("Testing game auto solve POST endpoint with invalid game ID...")
    url = "http://localhost:5000/api/game/auto_solve"
    payload = {
        "game_id": 9999,  # Assuming this game ID does not exist
        "user_id": 1,
        "security_token": "41c8fd33-f2c5-4406-a781-15328aa9dfb3"
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(url, json=payload, headers=headers)
    assert response.status_code == 405
    data = response.json()
    if print_debug_data:
        print(data)
    assert "result" in data
    assert data["result"] == "failure"
    assert data["message"] == "Invalid game id. Please send valid game_id value."
    assert "error" in data
    assert data["error"] == "Game id value does not exist."

if __name__ == "__main__":
    # Run the tests

    # Testing /api/user/register endpoint
    print("Starting tests for /api/user/register endpoint...")

    # Testing user registration with valid data
    test_register_new_user_post_success()
    # Validate presence of username and password
    test_register_new_user_post_missing_username()
    # Validate existing username
    test_register_new_user_post_user_exists()
    # Validate password format
    test_register_new_user_post_incorrect_password()
    # Validate username format
    test_register_new_user_post_incorrect_username()

    # Testing /api/user/login endpoint
    print("Starting tests for /api/user/login endpoint...")

    # Testing login with invalid credentials
    test_login_post_invalid_credentials()
    # Testing login with missing credentials
    test_login_post_missing_credentials()
    # Testing login with valid credentials
    test_login_post_success()

    # Testing /api/game/start endpoint
    print("Starting tests for /api/game/start endpoint...")

    # Testing game start with valid user
    test_game_start_post()
    # Testing game start with unknown user
    test_game_start_post_unknown_user()
    # Testing game start with invalid security token
    test_game_start_post_invalid_token()

    # Testing /api/game/guess_word endpoint
    print("Starting tests for /api/game/guess_word endpoint...")

    # Testing game guess word with invalid guess
    test_game_guess_word_post_invalid_guess()
    # Testing game guess word with invalid user
    test_game_guess_word_post_invalid_user()
    # Testing game guess word with invalid security token
    test_game_guess_word_post_invalid_security_token()
    # Testing game guess word with invalid game ID
    test_game_guess_word_post_invalid_game_id()
    # Testing game guess word with missing clue number
    test_game_guess_word_post_missing_clue_number()
    # Testing game guess word with missing guess word
    test_game_guess_word_post_missing_guess_word()
    # Testing game guess word with invalid clue number
    test_game_guess_word_post_invalid_clue_number()
    # Testing game guess word with already solved clue number
    test_game_guess_word_post_clue_number_already_solved()

    # Testing /api/game/solve_clue endpoint
    print("Starting tests for /api/game/guess_word endpoint...")

    # Testing game solve clue with invalid clue number
    test_game_solve_clue_post_invalid_clue_number()
    # Testing game solve clue with unknown user
    test_game_solve_clue_post_unknown_user()
    # Testing game solve clue with invalid security token
    test_game_solve_clue_post_invalid_security_token()
    # Testing game solve clue with invalid game ID
    test_game_solve_clue_post_invalid_game_id()
    # Testing game solve clue with missing clue number
    test_game_solve_clue_post_clue_number_is_missing()
    # Testing game solve clue with already solved clue number
    test_game_solve_clue_post_clue_number_is_already_solved()

    # Testing /api/game/auto_solve endpoint
    print("Starting tests for /api/game/auto_solve endpoint...")

    # Testing game auto solve with invalid security token
    test_game_auto_solve_post_invalid_security_token()
    # Testing game auto solve with invalid user
    test_game_auto_solve_post_invalid_user()
    # Testing game auto solve with invalid game ID
    test_game_auto_solve_post_invalid_game_id()