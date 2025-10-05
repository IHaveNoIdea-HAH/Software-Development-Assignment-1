from app.models.crossword import Crossword, Clue

class CrosswordService:
    @staticmethod
    def generate_crossword():
        # Placeholder: Generate a crossword puzzle
        grid = [['', '', ''], ['', '', ''], ['', '', '']]
        clues = [Clue(1, 'across', 'First clue', 'CAT')]
        return Crossword(grid, clues)

    @staticmethod
    def check_guess(crossword, guess):
        # Placeholder: Check if guess is correct
        return guess.upper() in [clue.answer for clue in crossword.clues]

