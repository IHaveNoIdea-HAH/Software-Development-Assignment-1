class CrosswordSchema:
    @staticmethod
    def dump(crossword):
        '''Serializes a Crossword object into a dictionary format suitable for JSON response to be sent to frontend.'''
        return {
            'grid': crossword.covered_grid,
            'clues': [
                {
                    'number': clue.number,
                    'direction': clue.direction,
                    'text': clue.text,
                    # 'answer': clue.answer # Exclude answer so that it is not exposed to frontend
                    'solved': clue.solved
                } for clue in crossword.clues
            ]
        }

    def dump_solved(crossword):
        '''Serializes a Crossword object including the solved grid into a dictionary format suitable for JSON response to be sent to frontend.'''
        return {
            'grid': crossword.solved_grid,
            'clues': [
                {
                    'number': clue.number,
                    'direction': clue.direction,
                    'text': clue.text,
                    'answer': clue.answer,
                    'solved': clue.solved
                } for clue in crossword.clues
            ]
        }

