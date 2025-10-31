from app.services.crossword_service import CrosswordService

class Game:
    def __init__(self, crossword, user_id, game_id, guess_limit):
        self.crossword = crossword
        self.user_id = user_id # to associate the game with a user
        self.game_id = game_id # unique identifier for the game session
        self.guess_limit = guess_limit # maximum number of guesses allowed
        self.score = 0 # player's score, can be updated as the game progresses
        self.status = 'started' # game status: 'started', 'completed'
        self.result = None # final result of the game, e.g., 'win', 'lose'
        self.solved_clues = [] # list to store solved clues
        self.guesses = [] # list to store player's guesses
        self.words_guessed = 0 # number of words guessed correctly

    def check_if_game_is_completed(self):
        '''
        Check if all clues in the crossword have been solved or if the guess limit has been reached.
        :return: True if all clues are solved or all guesses have been used, False otherwise
        '''
        if len(self.solved_clues) == len(self.crossword.clues):
            if self.score > 0:
                self.result = 'win'
            else:
                self.result = 'loss'
            self.status = 'completed'
            return True
        elif len(self.guesses) >= self.guess_limit:
            self.status = 'completed'
            self.result = 'loss'
            return True
        else:
            return False

    def is_status_completed(self):
        '''
        Check if the game status is 'completed'.
        :return: True if the game status is 'completed', False otherwise
        '''
        return self.status == 'completed'

    def is_game_won(self):
        '''
        Check if the game has been won by solving all clues.
        :return: True if the game is won, False otherwise
        '''
        return self.status == 'completed' and self.result == 'win'

    def auto_solve(self):
        '''
        Automatically solve the crossword by filling in all answers.
        :return:
        '''
        # Solve all unsolved clues and mark the game as completed with a loss
        for i in range(0, self.get_words_to_solve()):
            clue_number = self.get_crossword().clues[i].number
            if not self.check_clue_is_solved(clue_number):
                self.solve_clue(clue_number)

        self.status = 'completed'
        self.result = 'loss'  # Auto-solve results in a loss

    def get_user_id(self):
        '''
        Retrieve the user ID associated with the game.
        :return: user ID
        '''
        return self.user_id

    def get_game_id(self):
        '''
        Retrieve the game ID.
        :return: game ID
        '''
        return self.game_id

    def get_result(self):
        '''
        Retrieve the final result of the game.
        :return: final game result
        '''
        return self.result

    def get_status(self):
        '''
        Retrieve the current status of the game.
        :return: current game status
        '''
        return self.status

    def get_crossword(self):
        '''
        Retrieve the crossword associated with the game.
        :return: Crossword object
        '''
        return self.crossword

    def get_score(self):
        '''
        Retrieve the current score of the player.
        :return: current score
        '''
        return self.score

    def get_guesses_left(self):
        '''
        Retrieve the number of guesses left for the player.
        :return: number of guesses left
        '''
        return self.guess_limit - len(self.guesses)

    def get_guesses_made(self):
        '''
        Retrieve the number of guesses made by the player.
        :return: number of guesses made
        '''
        return len(self.guesses)

    def get_words_guessed(self):
        '''
        Retrieve the number of words guessed correctly by the player.
        :return: number of words guessed correctly
        '''
        return self.words_guessed

    def get_guess_limit(self):
        '''
        Retrieve the guess limit for the game.
        :return: guess limit
        '''
        return self.guess_limit

    def get_answer_for_clue(self, clue_number):
        '''
        Retrieve the answer for a specific clue number.
        :param clue_number: number of the clue to get the answer for
        :return: answer string
        '''
        if self.check_clue_number_is_valid(clue_number):
            return self.crossword.clues[clue_number - 1].answer
        else:
            raise ValueError("Invalid clue number provided.")

    def bump_score(self, points):
        '''
        Increase the player's score by the specified number of points.
        :param points: number of points to add to the score
        :return:
        '''
        self.score += points

    def check_clue_is_solved(self, clue_number):
        '''
        Check if the provided clue number has already been solved.
        :param clue_number: number of the clue to check
        :return: True if solved, False otherwise
        '''
        return clue_number in self.solved_clues

    def check_clue_number_is_valid(self, clue_number):
        '''
        Check if the provided clue number is valid for the current crossword.
        :param clue_number: number of the clue to check
        :return: True if valid, False otherwise
        '''
        return 0 < clue_number <= len(self.crossword.clues)

    def get_words_to_solve(self):
        '''
        Retrieve the total number of words to solve in the crossword.
        :return: total number of words
        '''
        return len(self.crossword.clues)

    def process_guess(self, clue_number, word_guess):
        '''
        Process a player's guess and update the game state accordingly.
        :param clue_number: number of the clue in the crossword to check the word_guess against
        :param word_guess: the word guess submitted by player
        :return: True if the guess is correct, False otherwise
        '''

        if self.check_clue_number_is_valid(clue_number):
            if CrosswordService.check_guess(self.crossword, word_guess, clue_number):
                # Correct guess so we mark the clue as solved
                self.solved_clues.append(clue_number)
                # Let's store the guess
                self.add_guess(clue_number, word_guess, True)
                # Let's bump the score
                self.bump_score(len(word_guess) * 10)  # Scoring: 10 points per letter
                # Increment words guessed count
                self.words_guessed += 1
                return True
            else:
                # Incorrect guess, let's store it
                self.add_guess(clue_number, word_guess, False)
                return False
        else:
            raise ValueError("Invalid clue number provided.")

    def solve_clue(self, clue_number):
        '''
        Solves a clue submitted by the player, updating the game state accordingly.
        :param clue_number: number of the clue in the crossword to check the word_guess against
        :return: answer string and penalty points applied
        '''

        if self.check_clue_number_is_valid(clue_number):
            answer = self.crossword.clues[clue_number - 1].answer.upper()
            # Correct guess so we mark the clue as solved
            self.solved_clues.append(clue_number)
            # Let's calculate penalty points
            penalty_points = -len(answer) * 10
            # Let's bump the score
            self.bump_score(penalty_points)  # Penalty: -10 points per letter
            # Increment words guessed count
            self.words_guessed += 1
            return answer, penalty_points
        else:
            raise ValueError("Invalid clue number provided.")

    def add_guess(self, clue_number, word_guess, is_correct):
        '''
        Add a player's guess to the guesses list.
        :param clue_number: number of the clue in the crossword
        :param word_guess: the word guessed by the player
        :param is_correct: boolean indicating if the guess was correct
        :return: None
        '''
        self.guesses.append({
            'clue_number': clue_number,
            'word_guess': word_guess.upper(),
            'is_correct': is_correct
        })

