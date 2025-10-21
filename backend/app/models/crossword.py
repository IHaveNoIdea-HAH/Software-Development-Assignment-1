class Crossword:
    def __init__(self, grid, clues):
        self.grid = grid  # 2D list
        self.clues = clues  # List of Clue objects

    def print_grid(self):
        for row in self.grid:
            print(' '.join(letter if letter else '.' for letter in row))

    def print_clues(self):
        for clue in self.clues:
            print(f"{clue.number} {clue.direction}: {clue.text} (Answer: {clue.answer})")

class Clue:
    def __init__(self, number, direction, text, answer):
        self.number = number
        self.direction = direction  # 'across' or 'down'
        self.text = text
        self.answer = answer

