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
    def load(self, data):
        return Game(
            user_id=data.get('user_id'),
            game_id=data.get('game_id'),
            crossword='' # CrosswordSchema.load(data.get('crossword')
        )
