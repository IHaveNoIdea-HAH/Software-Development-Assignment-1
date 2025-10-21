class Game:
    def __init__(self, crossword, user_id, game_id):
        self.crossword = crossword
        self.user_id = user_id # to associate the game with a user
        self.game_id = game_id # unique identifier for the game session
        self.start_time = None # current time when the game starts
        self.end_time = None # current time when the game ends
        self.score = 0 # player's score, can be updated as the game progresses
        self.status = 'started' # game status: 'started', 'paused', 'completed'
        self.result = None # final result of the game, e.g., 'win', 'lose'
        self.guesses = [] # list to store player's guesses
        self.letter_hints_used = 0 # number of letter hints used by the player
        self.word_hints_used = 0 # number of word hints used by the player
        self.time_taken = None # total time taken to complete the game
