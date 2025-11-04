from app.models.crossword import Crossword
from app.models.crossword import Clue

class CrosswordSchema:
    @staticmethod
    def dump(crossword):
        '''
        Serializes a Crossword object into a dictionary format suitable for JSON response to be sent to frontend.
        :param crossword: Crossword object to serialize
        :return: dictionary representation of the crossword
        '''

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

    @staticmethod
    def dump_solved(crossword):
        '''
        Serializes a Crossword object including the solved grid into a dictionary format suitable for JSON response to be sent to frontend.
        :param crossword: Crossword object to serialize
        :return: dictionary representation of the crossword with solved grid
        '''

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

    @staticmethod
    def dump_full(crossword):
        '''
        Serializes a Crossword object including both covered and solved grids into a dictionary format suitable for JSON response to be sent to frontend.
        :param crossword: Crossword object to serialize
        :return: dictionary representation of the crossword with both grids
        '''
        return {
            'covered_grid': crossword.covered_grid,
            'solved_grid': crossword.solved_grid,
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

    @staticmethod
    def load(data):
        '''
        Deserializes a dictionary representation of a Crossword object back into a Crossword object.
        :param data: dictionary representation of the crossword
        :return: Crossword object
        '''

        clues = []
        for clue_data in data['clues']:
            clue = Clue(
                number=clue_data['number'],
                direction=clue_data['direction'],
                text=clue_data['text'],
                answer=clue_data.get('answer', ''),
                solved=clue_data.get('solved', False)
            )
            clues.append(clue)

        crossword = Crossword(
            covered_grid=data['covered_grid'],
            solved_grid=data['solved_grid'],
            clues=clues
        )

        return crossword