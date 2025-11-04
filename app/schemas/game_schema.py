from app.models.game import Game
from app.schemas.crossword_schema import CrosswordSchema

class GameSchema:
    @staticmethod
    def dump(game):
        return {
            'user_id': game.user_id,
            'game_id': game.game_id,
            'crossword': CrosswordSchema.dump(game.crossword)
        }

    @staticmethod
    def dump_state(game):
        return {
            'game_id': game.get_game_id(),
            'game_status': game.get_status(),
            'game_result': game.get_result(),
            'current_score': game.get_score(),
            'guesses_made': game.get_guesses_made(),
            'guesses_left': game.get_guesses_left(),
            'words_solved': game.get_words_guessed(),
            'guess_limit': game.get_guess_limit(),
            'words_to_solve': game.get_words_to_solve()
        }

    @staticmethod
    def load(data):
        '''
        Deserializes a dictionary representation of a Game object back into a Game object.
        :param data: dictionary representation of the game
        :return: Game object
        '''

        crossword = CrosswordSchema.load(data['crossword'])

        game = Game(
            user_id=data['user_id'],
            game_id=data['game_id'],
            guess_limit=data['guess_limit'],
            score=data['score'],
            status=data['status'],
            result=data['result'],
            solved_clues=data['solved_clues'],
            guesses=data['guesses'],
            words_guessed=data['words_guessed'],
            crossword=crossword
        )

        return game

    @staticmethod
    def dump_full(game):
        '''
        Serializes a Game object including full details into a dictionary format suitable for JSON to be saved into JSON file for recovery when the app restarts.
        :param game:
        :return: dictionary representation of the game with full details
        '''
        return {
            'user_id': game.user_id,
            'game_id': game.game_id,
            'guess_limit': game.guess_limit,
            'score': game.score,
            'status': game.status,
            'result': game.result,
            'solved_clues': game.solved_clues,
            'guesses': game.guesses,
            'words_guessed': game.words_guessed,
            'crossword': CrosswordSchema.dump_full(game.crossword)
        }