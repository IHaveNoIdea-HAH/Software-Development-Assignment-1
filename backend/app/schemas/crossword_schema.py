class CrosswordSchema:
    @staticmethod
    def dump(crossword):
        return {
            'grid': crossword.grid,
            'clues': [
                {
                    'number': clue.number,
                    'direction': clue.direction,
                    'text': clue.text,
                    'answer': clue.answer
                } for clue in crossword.clues
            ]
        }

