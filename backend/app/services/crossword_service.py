from app.models.crossword import Crossword, Clue
from flask import current_app
import random


class CrosswordService:

    @staticmethod
    def generate_dummy_crossword():
        # this was very first dummy crossword used for testing purposes

        # Create a 20x20 empty grid
        grid = [['' for _ in range(20)] for _ in range(20)]

        # Place some Star Wars themed words
        # "JEDI" horizontally at row 0, col 0
        grid[0][0:4] = list('JEDI')
        # "SITH" vertically at row 2, col 2
        for i, letter in enumerate('SITH'):
            grid[2 + i][2] = letter
        # "YODA" horizontally at row 5, col 10
        grid[5][10:14] = list('YODA')
        # "FORCE" vertically at row 10, col 15
        for i, letter in enumerate('FORCE'):
            grid[10 + i][15] = letter
        # "LEIA" horizontally at row 12, col 5
        grid[12][5:9] = list('LEIA')

        clues = [
            Clue(1, 'across', 'Peacekeeper with a lightsaber', 'JEDI'),
            Clue(2, 'down', 'Dark side counterpart to Jedi', 'SITH'),
            Clue(3, 'across', 'Small green Jedi Master', 'YODA'),
            Clue(4, 'down', 'Energy that binds the galaxy', 'FORCE'),
            Clue(5, 'across', 'Princess and rebel leader', 'LEIA'),
        ]

        return Crossword(grid, clues)


    @staticmethod
    def generate_crossword(target_count_of_words=10):
        '''
        Generate a crossword puzzle with the specified target count of words.
        :param target_count_of_words:
        :return: Crossword object
        '''

        # Fetch the loaded word list
        words_clues = current_app.config['CROSSWORDS_DATA']
        if current_app.config['DEBUG']:
            print(f"Generating crossword with target of {target_count_of_words} words from a pool of {len(words_clues)} words.")

        # Let's initialize the grid
        grid_size = current_app.config['GRID_SIZE']
        covered_grid = [['' for _ in range(grid_size)] for _ in range(grid_size)]
        solved_grid = [['' for _ in range(grid_size)] for _ in range(grid_size)]

        # List to hold the clues
        clues = []

        # Numbering for clues
        picked_words_count = 0

        # this list is to check which words have already been picked to avoid duplicates
        # it contains the indexes of the words_clues list
        picked_words_indexes = []

        # number of attempts to fill a word onto the grid before we give up
        single_word_max_attempts = target_count_of_words * 10

        # Overall attempts counter for the entire grid filling process
        full_grid_max_attempts = target_count_of_words * 5000
        full_grid_attempts = 0

        # Let's try to fill the grid with words until we reach the target count
        while True:
            # increment overall attempts
            full_grid_attempts += 1

            # Initialize single word attempts counter for each word placement
            single_word_attempts = 0

            # Get random word index
            randowm_word_index = random.randint(0, len(words_clues) - 1)

            # Check if word already picked
            if randowm_word_index not in picked_words_indexes:

                # Let's try to place the word in the grid in random positions and directions constrained by single_word_max_attempts
                while single_word_attempts < single_word_max_attempts:
                    # increment attempts
                    single_word_attempts += 1

                    # now we need to check if the word can fit in the chosen position without conflicting
                    can_place = True

                    # let's make an attempt to place the word

                    # now we are going to randomly decide whether it is across or down
                    direction = random.choice(['across', 'down'])

                    # now we are going find random spot on the grid to place the word and take into account the direction
                    if direction == 'across':
                        # make sure the word fits in the grid
                        start_col = random.randint(0, grid_size - len(words_clues[randowm_word_index]['word']) - 1)
                        start_row = random.randint(0, grid_size - 1)
                    else:  # down
                        # make sure the word fits in the grid
                        start_col = random.randint(0, grid_size - 1)
                        start_row = random.randint(0, grid_size - len(words_clues[randowm_word_index]['word']) - 1)

                    for i, letter in enumerate(words_clues[randowm_word_index]['word'].upper()):
                        if direction == 'across':
                            if solved_grid[start_row][start_col + i] not in ('', letter):
                                can_place = False
                        else:  # down
                            if solved_grid[start_row + i][start_col] not in ('', letter):
                                can_place = False

                    # If it can be placed, we place it
                    if can_place:
                        picked_words_indexes.append(randowm_word_index)
                        picked_words_count = len(picked_words_indexes)
                        if direction == 'across':
                            for i, letter in enumerate(words_clues[randowm_word_index]['word'].upper()):
                                solved_grid[start_row][start_col + i] = letter
                                if i == 0:
                                    covered_grid[start_row][start_col] = str(picked_words_count)
                                else:
                                    covered_grid[start_row][start_col + i] = '[]'
                        else:  # down
                            for i, letter in enumerate(words_clues[randowm_word_index]['word'].upper()):
                                solved_grid[start_row + i][start_col] = letter
                                if i == 0:
                                    covered_grid[start_row][start_col] = str(picked_words_count)
                                else:
                                    covered_grid[start_row + i][start_col] = '[]'

                        # Add the clue for this word we've placed onto the grid
                        clues.append(Clue(picked_words_count, direction, words_clues[randowm_word_index]['clue'], words_clues[randowm_word_index]['word'].upper()))
                        if current_app.config['DEBUG']:
                            print(f"Attempt {single_word_attempts}, placed word '{words_clues[randowm_word_index]['word'].upper()}' as clue number {picked_words_count} {direction} at row {start_row}, col {start_col}.")
                        break  # exit the while attempts loop as we have placed the word

            # check if we have exceeded max attempts to fill up the grid
            if full_grid_attempts >= full_grid_max_attempts:
                if current_app.config['DEBUG']:
                    print("Max attempts reached while trying to fill up the the grid, stopping.")
                break

            # check if we have reached the target count of words and can stop the while loop
            if picked_words_count >= target_count_of_words:
                if current_app.config['DEBUG']:
                    print(f"Overall attempt {full_grid_attempts}, reached target of {target_count_of_words} words to place in the grid.")
                break

        return Crossword(solved_grid, covered_grid, clues)


    @staticmethod
    def check_guess(crossword, guess, clue_number):
        '''
        Check if the provided guess for the given clue number is correct.
        :param crossword: the crossword object
        :param guess: the word guess submitted by player
        :param clue_number: number of the clue in the crossword to check the word guess against
        :return:
        '''
        # Check if guess is correct
        return guess.upper() == crossword.clues[clue_number - 1].answer.upper()


    @staticmethod
    def solve_clue(crossword, clue_number):
        '''
        Solves a clue in the crossword by copying the answer from the solved grid to the covered grid.
        :param crossword: the crossword object
        :param clue_number: number of the clue in the crossword to solve
        :return: answer string
        '''
        clue = crossword.clues[clue_number - 1]
        answer = clue.answer.upper()

        # Now we need to find where this clue is located on the grid
        grid_size = len(crossword.solved_grid)

        found = False

        for row in range(grid_size):
            for col in range(grid_size):
                if crossword.covered_grid[row][col] == str(clue_number):
                    # We found the starting position of the clue
                    if clue.direction == 'across':
                        for i in range(len(answer)):
                            crossword.covered_grid[row][col + i] = answer[i]
                    else:  # down
                        for i in range(len(answer)):
                            crossword.covered_grid[row + i][col] = answer[i]
                    found = True
                    break
            if found:
                break

        return answer
