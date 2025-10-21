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
        # Load (or reuse) the cached word list
        words_clues = current_app.config['CROSSWORDS_DATA']

        # Shuffle and pick a subset
        random.shuffle(words_clues)
        selected = words_clues[:target_count_of_words]  # Adjust count as needed

        # Let's initialize the grid
        grid_size = current_app.config['GRID_SIZE']
        grid = [['' for _ in range(grid_size)] for _ in range(grid_size)]

        # Split into across/down words
        half = len(selected) // 2
        across_words = selected[:half]
        down_words = selected[half:]

        def place_across(word, row, col):
            for i, letter in enumerate(word):
                if col + i < grid_size:
                    grid[row][col + i] = letter

        def place_down(word, row, col):
            for i, letter in enumerate(word):
                if row + i < grid_size:
                    grid[row + i][col] = letter

        # Place words
        for entry in across_words:
            word = entry['word'].upper()
            row = random.randint(0, grid_size - 1)
            col = random.randint(0, grid_size - len(word))
            place_across(word, row, col)

        for entry in down_words:
            word = entry['word'].upper()
            row = random.randint(0, grid_size - len(word))
            col = random.randint(0, grid_size - 1)
            place_down(word, row, col)

        # Generate clues
        clues = []
        num = 1
        for entry in across_words:
            clues.append(Clue(num, 'across', entry['clue'], entry['word']))
            num += 1
        for entry in down_words:
            clues.append(Clue(num, 'down', entry['clue'], entry['word']))
            num += 1

        return Crossword(grid, clues)


    @staticmethod
    def check_guess(crossword, guess):
        # Placeholder: Check if guess is correct
        return guess.upper() in [clue.answer for clue in crossword.clues]
