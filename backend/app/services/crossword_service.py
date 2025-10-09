from app.models.crossword import Crossword, Clue

class CrosswordService:
    @staticmethod
    def generate_crossword():
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
    def check_guess(crossword, guess):
        # Placeholder: Check if guess is correct
        return guess.upper() in [clue.answer for clue in crossword.clues]
