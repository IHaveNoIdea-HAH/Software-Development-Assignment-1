class Config:
    SECRET_KEY = 'your-secret-key'
    DEBUG = True
    # Here we have our variables to store the state of our app
    DATA_FOLDER_PATH = ''  # Path to the JSON file with crossword words
    CROSSWORDS_DATA = {} # This will hold our loaded JSON data to generate crosswords
    USERS = {} # In-memory users storage
    LAST_USER_ID = 0  # Counter for user IDs
    GAME_ID = 1  # Counter for game sessions
    GRID_SIZE = 15  # Size of the crossword grid
    GAME_DIFFICULTY_LEVEL = {
        'normal': 10,  # Default game difficulty level
        'hard': 15,  # More words for harder level
        'easy': 5  # Fewer words for easier level
    }
    GAMES = {} # In-memory games storage