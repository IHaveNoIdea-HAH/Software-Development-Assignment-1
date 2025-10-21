from flask import Blueprint, request, jsonify, current_app
from app.services.crossword_service import CrosswordService
from app.schemas.crossword_schema import CrosswordSchema
from app.models.game import Game
from app.models.crossword import Crossword

game_bp = Blueprint('game', __name__)

@game_bp.route('/start', methods=['POST'])
def start_game():
    try:
        # Let's retrieve the JSON payload from the request body of the POST request
        data = request.get_json()

        # Let's check if frontend sent a game difficulty level
        game_level = data.get('gameDifficultyLevel', 'normal')
        user_id = data.get('userId', -1)

        # Check if user is known
        if user_id == -1 or user_id not in current_app.config['USERS']:
            # Unknown user, cannot start game
            return jsonify({
                'result': 'failure',
                'message': 'Unknown user. Please log in to start a game.',
                'error': 'Unknown User ID has been received.'
            }), 400
        else:
            target_count_of_words = current_app.config['GAME_DIFFICULTY_LEVEL'].get(game_level.lower(), 10)

            # Generate a new crossword using the CrosswordService
            crossword = CrosswordService.generate_crossword(target_count_of_words)

            # For debugging: print the grid and clues to console
            # That's what is going to be sent back to frontend
            crossword.print_grid()
            crossword.print_clues()

            # Assign a unique game_id and increment the global GAME_ID counter in our config
            game_id = current_app.config['GAME_ID']
            current_app.config['GAME_ID'] += 1

            # Create a new Game instance and store it in the GAMES dictionary
            new_game = Game(crossword, user_id, game_id)
            current_app.config['GAMES'][game_id] = new_game

            # Create response we are going to send back to frontend
            # Serialize crossword using CrosswordSchema
            return jsonify({
                'result': 'success',
                'message': 'Game started',
                'game_id': game_id,
                'crossword': CrosswordSchema.dump(crossword)
            }), 200
    except Exception as e:
        return jsonify({
            'result': 'failure',
            'message': 'Error starting game',
            'error': str(e)
        }), 500

@game_bp.route('/guess', methods=['POST'])
def guess_word():
    # Placeholder: Check a guessed word
    return jsonify({'message': 'Guess received'})

@game_bp.route('/status/<int:game_id>', methods=['GET'])
def game_status(game_id):
    # Placeholder: Return game status
    return jsonify({'game_id': game_id, 'status': 'in_progress'})

@game_bp.route('/welcome', methods=['GET'])
def game_welcome():
    # Placeholder: Returns welcome message
    return jsonify({'welcome_message': 'Hello and welcome to our cool crossword game', 'status': 'running'})
