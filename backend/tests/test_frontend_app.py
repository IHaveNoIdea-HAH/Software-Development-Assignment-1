import streamlit as st
import requests
import pandas as pd

# Set the title of the app
st.title("Crossword Game App")
st.set_page_config(layout="wide") # Use wide layout for better grid display

# Create a sidebar menu
menu = st.sidebar.radio("Menu", ["Register", "Login", "New Game", "Guess Word", "Auto Solve", "Solve Clue", "Game State"])
host = st.text_input("Enter the host", value="http://localhost:5000")

# Define the behavior for each menu item
if menu == "Register":
    st.header("Register")
    username = st.text_input("Enter your username")
    password = st.text_input("Enter your password", type="password")
    email = st.text_input("Enter your email")

    if st.button("Register"):
        payload = {
            "username": username,
            "password": password,
            "email": email
        }
        headers = {
            "Content-Type": "application/json"
        }
        url = f"{host}/api/user/register"
        response = requests.post(url, json=payload, headers=headers)
        data = response.json()
        st.write("Response:", data)

        if response.status_code == 200:
            st.success(f"User {username} registered successfully!")

            # Store security token in st.session_state so that it can be used to start a new game
            if "security_token" not in st.session_state:
                st.session_state["security_token"] = data["security_token"]
            # Store user_id in st.session_state so that it can be used to start a new game
            if "user_id" not in st.session_state:
                st.session_state["user_id"] = data["user_id"]
            # Store username in st.session_state
            if "username" not in st.session_state:
                st.session_state["username"] = data["username"]
        else:
            st.error(f"{response.status_code}: Failed to register user {username}. Error: {response.text}")




elif menu == "Login":
    st.header("Login")
    login_name = st.text_input("Enter your username")
    login_password = st.text_input("Enter your password", type="password")

    if st.button("Login"):
        payload = {
            "username": login_name,
            "password": login_password
        }
        headers = {
            "Content-Type": "application/json"
        }
        url = f"{host}/api/user/login"
        response = requests.post(url, json=payload, headers=headers)
        data = response.json()
        st.write("Response:", data)

        if response.status_code == 200:
            st.success(f"User {login_name} logged in successfully!")

            # Store security token in st.session_state so that it can be used to start a new game
            if "security_token" not in st.session_state:
                st.session_state["security_token"] = data["security_token"]
            # Store user_id in st.session_state so that it can be used to start a new game
            if "user_id" not in st.session_state:
                st.session_state["user_id"] = data["user_id"]
            # Store username in st.session_state
            if "username" not in st.session_state:
                st.session_state["username"] = data["username"]
        else:
            st.error(f"{response.status_code}: Failed to log in user {login_name}. Error: {response.text}")

elif menu == "New Game":
    st.header("New Game")
    difficulty = st.selectbox("Select difficulty level", ["Easy", "Normal", "Hard"])

    if st.button("Start Game"):
        payload = {
            "game_difficulty_level": difficulty.lower(),
            "user_id": st.session_state.get("user_id", -1),
            "security_token": st.session_state.get("security_token", "")
        }
        headers = {
            "Content-Type": "application/json"
        }
        url = f"{host}/api/game/start"
        response = requests.post(url, json=payload, headers=headers)
        data = response.json()

        st.write("Response:", data)

        if response.status_code == 200:
            st.success(f"Game started successfully! Game ID: {data['game_state']['game_id']}")
            st.success(f"New game started with difficulty: {difficulty}")

            # Store game_id in st.session_state
            if "game_id" not in st.session_state:
                st.session_state["game_id"] = data['game_state']["game_id"]

            # Store crossword in st.session_state
            if "crossword" not in st.session_state:
                st.session_state["crossword"] = data["crossword"]
        else:
            st.error(f"{response.status_code}: Failed to start new game. Error: {response.text}")

    if "crossword" in st.session_state:
        df = pd.DataFrame(st.session_state["crossword"]["grid"])

        # st.header("Using st.dataframe")
        # st.dataframe(df)

        st.header("Crossword Grid")
        st.table(df)

        st.write("---")

elif menu == "Guess Word":
    st.header("Guess Word")
    clue_number = st.number_input("Enter clue number", min_value=1, step=1)
    word_guess = st.text_input("Enter your word guess")

    if st.button("Submit Guess"):
        payload = {
            "clue_number": clue_number,
            "word_guess": word_guess,
            "game_id": st.session_state.get("game_id", -1),
            "user_id": st.session_state.get("user_id", -1),
            "security_token": st.session_state.get("security_token", "")
        }
        headers = {
            "Content-Type": "application/json"
        }
        url = f"{host}/api/game/guess_word"
        response = requests.post(url, json=payload, headers=headers)
        data = response.json()
        st.write("Response:", data)

        if response.status_code == 200:
            if data["is_correct"]:
                st.success(f"Correct guess for clue number {clue_number}!")
            else:
                st.warning(f"Incorrect guess for clue number {clue_number}. Try again!")
        else:
            st.error(f"{response.status_code}: Failed to submit guess. Error: {response.text}")

elif menu == "Auto Solve":
    st.header("Auto Solve")
    if st.button("Auto Solve the Crossword"):
        payload = {
            "game_id": st.session_state.get("game_id", -1),
            "user_id": st.session_state.get("user_id", -1),
            "security_token": st.session_state.get("security_token", "")
        }
        headers = {
            "Content-Type": "application/json"
        }
        url = f"{host}/api/game/auto_solve"
        response = requests.post(url, json=payload, headers=headers)
        data = response.json()
        st.write("Response:", data)

        if response.status_code == 200:
            st.success("Crossword auto-solved successfully!")
            df = pd.DataFrame(data["crossword"]["grid"])

            st.header("Crossword Grid")
            st.table(df)

        else:
            st.error(f"{response.status_code}: Failed to auto-solve crossword. Error: {response.text}")

elif menu == "Solve Clue":
    st.header("Solve Clue")
    clue_number = st.number_input("Enter clue number to solve", min_value=1, step=1)

    if st.button("Solve Clue"):
        payload = {
            "clue_number": clue_number,
            "game_id": st.session_state.get("game_id", -1),
            "user_id": st.session_state.get("user_id", -1),
            "security_token": st.session_state.get("security_token", "")
        }
        headers = {
            "Content-Type": "application/json"
        }
        url = f"{host}/api/game/solve_clue"
        response = requests.post(url, json=payload, headers=headers)
        data = response.json()
        st.write("Response:", data)

        if response.status_code == 200:
            st.success(f"Clue number {clue_number} solved successfully, answer {data['answer']} and penalty points {data['penalty_points']}!")

        else:
            st.error(f"{response.status_code}: Failed to solve clue. Error: {response.text}")

elif menu == "Game State":
    st.header("Game State")

    game_id = st.text_input("Enter Game ID", value=st.session_state.get("game_id", ""))

    if st.button("Get Game State"):
        url = f"{host}/api/game/game_status/" + str(game_id)
        response = requests.get(url)
        data = response.json()
        st.write("Response:", data)

        if response.status_code == 200:
            st.success("Game state retrieved successfully!")
            st.json(data["game_state"])
        else:
            st.error(f"{response.status_code}: Failed to retrieve game state. Error: {response.text}")