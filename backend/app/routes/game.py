from flask import Blueprint, request, jsonify, current_app, render_template
from app.services.crossword_service import CrosswordService 
from app.schemas.crossword_schema import CrosswordSchema 
from app.models.game import Game
from app.models.crossword import Crossword
import json
import random
import os

game_bp = Blueprint('game', __name__)

@game_bp.route('/start', methods=['POST']) #to access these you must do /api/game/[route] (example: http://192.168.0.15:5000/api/game/welcome)
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

@game_bp.route('/test', methods=['GET'])
def game_test():
    return render_template('Test.html') #Remember to change the html to something else

@game_bp.route('/random-word', methods=['GET']) #Gets a random word
def random_word():
    json_path = os.path.join(current_app.root_path, 'data', 'crossword_words.json') #Gets words from data folder, crossword json file
    try:
        with open(json_path, 'r') as f: #Loads json
            words = json.load(f)
        
        if words: #If the word has been located choose a random word from there
            chosen = random.choice(words)
            return jsonify(chosen), 200
        else:
            return jsonify({'error': 'No words found'}), 404 #If no words has been found, cause error.
    except FileNotFoundError: #Ensures we input json file in the correct place
        return jsonify({'error': 'JSON file not found at ' + json_path}), 404
   
