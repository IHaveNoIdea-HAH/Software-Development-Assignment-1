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
    def load(self, data):
        return Game(
            user_id=data.get('user_id'),
            game_id=data.get('game_id'),
            crossword='' # CrosswordSchema.load(data.get('crossword')
        )
