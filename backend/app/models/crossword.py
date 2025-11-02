class Crossword:
    def __init__(self, solved_grid, covered_grid, clues):
        self.solved_grid = solved_grid  # 2D list
        self.covered_grid = covered_grid  # 2D list
        self.clues = clues  # List of Clue objects

    def print_covered_grid(self):
        print()
        for row in self.covered_grid:
            print(' '.join(letter if letter else '.' for letter in row))

    def print_solved_grid(self):
        print()
        for row in self.solved_grid:
            print(' '.join(letter if letter else '.' for letter in row))

    def print_clues(self):
        print()
        for clue in self.clues:
            print(f"{clue.number} {clue.direction}: {clue.text} (Answer: {clue.answer})")

class Clue:
    def __init__(self, number, direction, text, answer, solved=False):
        self.number = number
        self.direction = direction  # 'across' or 'down'
        self.text = text
        self.answer = answer
        self.solved = False

