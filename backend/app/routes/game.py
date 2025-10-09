from flask import Blueprint, request, jsonify
from app.services.crossword_service import CrosswordService
from app.schemas.crossword_schema import CrosswordSchema

# In-memory game ID counter (for demonstration only)
game_id_counter = 1

game_bp = Blueprint('game', __name__)

@game_bp.route('/start', methods=['POST'])
def start_game():
    global game_id_counter
    # Generate a new crossword using the CrosswordService
    crossword = CrosswordService.generate_crossword()
    # Assign a unique game_id and increment the counter
    game_id = game_id_counter
    game_id_counter += 1
    # Serialize crossword using CrosswordSchema
    response = {
        'message': 'Game started',
        'game_id': game_id,
        'crossword': CrosswordSchema.dump(crossword)
    }
    return jsonify(response)

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
