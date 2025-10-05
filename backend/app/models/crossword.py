class Crossword:
    def __init__(self, grid, clues):
        self.grid = grid  # 2D list
        self.clues = clues  # List of Clue objects

class Clue:
    def __init__(self, number, direction, text, answer):
        self.number = number
        self.direction = direction  # 'across' or 'down'
        self.text = text
        self.answer = answer

