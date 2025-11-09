class Config:
    DEBUG = True
    # Here we have our variables to store the state of our app
    DATA_FOLDER_PATH = ''  # Path to the JSON file with crossword words
    CROSSWORDS_DATA = {} # This will hold our loaded JSON data to generate crosswords
    USERS = {} # In-memory users storage
    LAST_USER_ID = 0  # Counter for user IDs
    GAME_ID = 1  # Counter for game sessions
    GRID_SIZE = 20  # Size of the crossword grid
    GAME_DIFFICULTY_LEVEL = {
        'normal': {
            "words": 10,  # Default game difficulty level
            "guess_limit": 20  # Default guess limit
        },
        'hard': {
            "words": 15,  # More words for harder level
            "guess_limit": 20  # Fewer guesses allowed
        },
        'easy': {
            "words": 5, # Fewer words for easier level
            "guess_limit": 30  # More guesses allowed
        }
    }
    GAMES = {} # In-memory games storage