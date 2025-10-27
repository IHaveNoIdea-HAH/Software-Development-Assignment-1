from app.models.crossword import Crossword, Clue
from flask import current_app
import random


class CrosswordService:

    @staticmethod
    def generate_dummy_crossword():
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
        # Fetch the loaded word list
        words_clues = current_app.config['CROSSWORDS_DATA']

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

        # Offset to manage placement in grid
        offset = 0

        # Let's fill top left corner with word
        # filling 1st word across
        # let's get a random word not already picked
        while True:
            randowm_word_index = random.randint(0, len(words_clues) - 1)
            if randowm_word_index not in picked_words_indexes and len(words_clues[randowm_word_index]['word']) < grid_size - 2 * offset:
                picked_words_indexes.append(randowm_word_index)
                picked_words_count = len(picked_words_indexes)
                y_index = offset
                for i, letter in enumerate(words_clues[randowm_word_index]['word'].upper()):
                    solved_grid[y_index][offset + i] = letter
                    if i == 0:
                        covered_grid[y_index][offset] = str(picked_words_count)
                    else:
                        covered_grid[y_index][offset + i] = '[]'
                clues.append(Clue(picked_words_count, 'across', words_clues[randowm_word_index]['clue'], words_clues[randowm_word_index]['word'].upper()))
                break

        # Let's fill bottom left corner with word
        # filling 1st word across
        # let's get a random word not already picked
        while True:
            randowm_word_index = random.randint(0, len(words_clues) - 1)
            if randowm_word_index not in picked_words_indexes and len(words_clues[randowm_word_index]['word']) < grid_size - 2 * offset:
                picked_words_indexes.append(randowm_word_index)
                picked_words_count = len(picked_words_indexes)
                y_index = grid_size - offset -1
                for i, letter in enumerate(words_clues[randowm_word_index]['word'].upper()):
                    solved_grid[y_index][offset + i] = letter
                    if i == 0:
                        covered_grid[y_index][offset] = str(picked_words_count)
                    else:
                        covered_grid[y_index][offset + i] = '[]'
                clues.append(Clue(picked_words_count, 'across', words_clues[randowm_word_index]['clue'], words_clues[randowm_word_index]['word'].upper()))
                break

        # Let's fill top right corner with word
        # filling word across
        # let's get a random word not already picked
        while True:
            randowm_word_index = random.randint(0, len(words_clues) - 1)
            if randowm_word_index not in picked_words_indexes and len(words_clues[randowm_word_index]['word']) < grid_size - 2 * offset:
                picked_words_indexes.append(randowm_word_index)
                picked_words_count = len(picked_words_indexes)
                y_index = offset
                x_index = grid_size - offset - len(words_clues[randowm_word_index]['word'])
                for i, letter in enumerate(words_clues[randowm_word_index]['word'].upper()):
                    solved_grid[y_index][x_index + i] = letter
                    if i == 0:
                        covered_grid[y_index][x_index] = str(picked_words_count)
                    else:
                        covered_grid[y_index][x_index + i] = '[]'
                clues.append(Clue(picked_words_count, 'across', words_clues[randowm_word_index]['clue'], words_clues[randowm_word_index]['word'].upper()))
                break


        # Let's fill bottom right corner with word
        # filling word across
        # let's get a random word not already picked
        while True:
            randowm_word_index = random.randint(0, len(words_clues) - 1)
            if randowm_word_index not in picked_words_indexes and len(words_clues[randowm_word_index]['word']) < grid_size - 2 * offset:
                picked_words_indexes.append(randowm_word_index)
                picked_words_count = len(picked_words_indexes)
                y_index = grid_size - offset -1
                x_index = grid_size - offset - len(words_clues[randowm_word_index]['word'])
                for i, letter in enumerate(words_clues[randowm_word_index]['word'].upper()):
                    solved_grid[y_index][x_index + i] = letter
                    if i == 0:
                        covered_grid[y_index][x_index] = str(picked_words_count)
                    else:
                        covered_grid[y_index][x_index + i] = '[]'
                clues.append(Clue(picked_words_count, 'across', words_clues[randowm_word_index]['clue'], words_clues[randowm_word_index]['word'].upper()))
                break

        # ToDo: Continue filling the grid with more words until target_count_of_words is reached


        return Crossword(solved_grid, covered_grid, clues)


    @staticmethod
    def check_guess(crossword, guess):
        # Placeholder: Check if guess is correct
        return guess.upper() in [clue.answer for clue in crossword.clues]
