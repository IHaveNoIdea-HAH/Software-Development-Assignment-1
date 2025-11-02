from flask import Blueprint, request, jsonify, current_app, render_template
from app.services.crossword_service import CrosswordService
from app.schemas.crossword_schema import CrosswordSchema
from app.schemas.game_schema import GameSchema
from app.models.game import Game
from app.models.crossword import Crossword
from app.utils.helpers import save_games_to_json
import json
import random
import os

game_bp = Blueprint('game', __name__)

@game_bp.route('/start', methods=['POST']) #to access these you must do /api/game/[route] (example: http://192.168.0.15:5000/api/game/welcome)
def start_game():
    try:
        # Let's retrieve the JSON payload from the request body of the POST request
        data = request.get_json()

        if current_app.config['DEBUG']:
            print("Received data for starting game:", data)

        # Let's check if frontend sent a game difficulty level
        game_level = data.get('game_difficulty_level', 'normal')
        user_id = data.get('user_id', -1)
        security_token = data.get('security_token', -1)

        # Check if user is known
        if user_id == -1 or user_id not in current_app.config['USERS']:
            # Unknown user, cannot start game
            return jsonify({
                'result': 'failure',
                'message': 'Unknown user. Please log in to start a game.',
                'error': 'Unknown User ID has been received.'
            }), 400
        elif security_token != current_app.config['USERS'][user_id].security_token:
            # Invalid security token
            return jsonify({
                'result': 'failure',
                'message': 'Invalid security token. Please log in again.',
                'error': 'Security token does not match.'
            }), 403
        else:
            target_count_of_words = current_app.config['GAME_DIFFICULTY_LEVEL'][game_level.lower()]["words"]
            guess_limit = current_app.config['GAME_DIFFICULTY_LEVEL'][game_level.lower()]["guess_limit"]

            # Generate a new crossword using the CrosswordService
            crossword = CrosswordService.generate_crossword(target_count_of_words)

            # For debugging: print the grid and clues to console
            # That's what is going to be sent back to frontend
            if current_app.config['DEBUG']:
                crossword.print_clues()
                crossword.print_covered_grid()
                crossword.print_solved_grid()

            # Assign a unique game_id and increment the global GAME_ID counter in our config
            game_id = current_app.config['GAME_ID']
            current_app.config['GAME_ID'] += 1

            # Create a new Game instance and store it in the GAMES dictionary
            g = Game(crossword, user_id, game_id, guess_limit)
            current_app.config['GAMES'][game_id] = g

            # Save active games to JSON file for recovery after restart
            save_games_to_json()

            # Create response we are going to send back to frontend
            # Serialize crossword using CrosswordSchema
            return jsonify({
                'result': 'success',
                'message': 'Game started',
                'user_id': user_id,
                'crossword': CrosswordSchema.dump(crossword),
                'game_state': GameSchema.dump_state(g),
            }), 200
    except Exception as e:
        return jsonify({
            'result': 'failure',
            'message': 'Error starting game',
            'error': str(e)
        }), 500

@game_bp.route('/guess_word', methods=['POST'])
def guess_word():
    try:
        # Let's retrieve the JSON payload from the request body of the POST request
        data = request.get_json()

        clue_number = data.get('clue_number', -1)
        word_guess = data.get('word_guess', '')
        game_id = data.get('game_id', -1)
        user_id = data.get('user_id', -1)
        security_token = data.get('security_token', -1)

        # Check if user is known
        if user_id == -1 or user_id not in current_app.config['USERS']:
            # Unknown user, cannot start game
            return jsonify({
                'result': 'failure',
                'message': 'Unknown user. Please log in to start a game.',
                'error': 'Unknown User ID has been received.'
            }), 400
        elif security_token != current_app.config['USERS'][user_id].security_token:
            # Invalid security token
            return jsonify({
                'result': 'failure',
                'message': 'Invalid security token. Please log in again.',
                'error': 'Security token does not match.'
            }), 403
        elif game_id not in current_app.config['GAMES']:
            # Invalid game_id
            return jsonify({
                'result': 'failure',
                'message': 'Invalid game id. Please send valid game_id value.',
                'error': 'Game id value does not exist.'
            }), 405
        elif current_app.config['GAMES'][game_id].is_status_completed():
            return jsonify({
                'result': 'failure',
                'message': 'Game is already completed. No more actions allowed.',
                'error': 'Game already completed.'
            }), 408
        elif clue_number == -1:
            return jsonify({
                'result': 'failure',
                'message': 'clue_number is required.',
                'error': 'Missing clue_number.'
            }), 400
        elif word_guess == '':
            return jsonify({
                'result': 'failure',
                'message': 'word_guess is required.',
                'error': 'Missing word_guess.'
            }), 400
        elif not current_app.config['GAMES'][game_id].check_clue_number_is_valid(clue_number):
            return jsonify({
                'result': 'failure',
                'message': 'Invalid clue number provided.',
                'error': 'clue_number is invalid.'
            }), 406
        elif current_app.config['GAMES'][game_id].check_clue_is_solved(clue_number):
            return jsonify({
                'result': 'failure',
                'message': 'Clue number has already been solved.',
                'error': 'clue_number already solved.'
            }), 407
        else:
            # Retrieve the game instance
            g = current_app.config['GAMES'][game_id]
            # Process the guess
            is_correct, points_scored = g.process_guess(clue_number, word_guess)
            answer = ''

            # check if game is over
            if g.check_if_game_is_completed():
                if g.is_game_won():
                    message = 'You have won the game!'
                else:
                    message = 'You have lost!'
            else:
                if is_correct:
                    message = 'Correct guess!'
                    answer = g.get_answer_for_clue(clue_number)
                else:
                    message = 'Incorrect guess.'

            # Save active games to JSON file for recovery after restart
            save_games_to_json()

            # Create response we are going to send back to frontend
            return jsonify({
                'result': 'success',
                'message': message,
                'is_correct': is_correct,
                'answer': answer,
                'points_scored': points_scored,
                'game_state': GameSchema.dump_state(g),
                'crossword': CrosswordSchema.dump(g.get_crossword())
            }), 200
    except Exception as e:
        return jsonify({
            'result': 'failure',
            'message': 'Error processing word guess',
            'error': str(e)
        }), 500

@game_bp.route('/solve_clue', methods=['POST'])
def solve_clue():
    try:
        # Let's retrieve the JSON payload from the request body of the POST request
        data = request.get_json()

        clue_number = data.get('clue_number', -1)
        game_id = data.get('game_id', -1)
        user_id = data.get('user_id', -1)
        security_token = data.get('security_token', -1)

        # Check if user is known
        if user_id == -1 or user_id not in current_app.config['USERS']:
            # Unknown user, cannot start game
            return jsonify({
                'result': 'failure',
                'message': 'Unknown user. Please log in to start a game.',
                'error': 'Unknown User ID has been received.'
            }), 400
        elif security_token != current_app.config['USERS'][user_id].security_token:
            # Invalid security token
            return jsonify({
                'result': 'failure',
                'message': 'Invalid security token. Please log in again.',
                'error': 'Security token does not match.'
            }), 403
        elif game_id not in current_app.config['GAMES']:
            # Invalid game_id
            return jsonify({
                'result': 'failure',
                'message': 'Invalid game id. Please send valid game_id value.',
                'error': 'Game id value does not exist.'
            }), 405
        elif current_app.config['GAMES'][game_id].is_status_completed():
            return jsonify({
                'result': 'failure',
                'message': 'Game is already completed. No more actions allowed.',
                'error': 'Game already completed.'
            }), 408
        elif clue_number == -1:
            return jsonify({
                'result': 'failure',
                'message': 'clue_number is required.',
                'error': 'Missing clue_number.'
            }), 400
        elif not current_app.config['GAMES'][game_id].check_clue_number_is_valid(clue_number):
            return jsonify({
                'result': 'failure',
                'message': 'Invalid clue number provided.',
                'error': 'clue_number is invalid.'
            }), 406
        elif current_app.config['GAMES'][game_id].check_clue_is_solved(clue_number):
            return jsonify({
                'result': 'failure',
                'message': 'Clue number has already been solved.',
                'error': 'clue_number already solved.'
            }), 407
        else:
            # Retrieve the game instance
            g = current_app.config['GAMES'][game_id]
            # Process the guess
            answer, penalty_points = g.solve_clue(clue_number)

            # Check if game is completed
            if g.check_if_game_is_completed():
                if g.is_game_won():
                    message = 'You have won the game!'
                else:
                    message = 'You have lost!'
            else:
                message = 'Clue solved successfully.'

            # Save active games to JSON file for recovery after restart
            save_games_to_json()

            # Create response we are going to send back to frontend
            return jsonify({
                'result': 'success',
                'message': message,
                'answer': answer,
                'penalty_points': penalty_points,
                'game_state': GameSchema.dump_state(g),
                'crossword': CrosswordSchema.dump(g.get_crossword())
            }), 200
    except Exception as e:
        return jsonify({
            'result': 'failure',
            'message': 'Error processing solve clue',
            'error': str(e)
        }), 500


@game_bp.route('/auto_solve', methods=['POST'])
def auto_solve():
    try:
        # Let's retrieve the JSON payload from the request body of the POST request
        data = request.get_json()

        game_id = data.get('game_id', -1)
        user_id = data.get('user_id', -1)
        security_token = data.get('security_token', -1)

        # Check if user is known
        if user_id == -1 or user_id not in current_app.config['USERS']:
            # Unknown user, cannot start game
            return jsonify({
                'result': 'failure',
                'message': 'Unknown user. Please log in to start a game.',
                'error': 'Unknown User ID has been received.'
            }), 400
        elif security_token != current_app.config['USERS'][user_id].security_token:
            # Invalid security token
            return jsonify({
                'result': 'failure',
                'message': 'Invalid security token. Please log in again.',
                'error': 'Security token does not match.'
            }), 403
        elif game_id not in current_app.config['GAMES']:
            # Invalid game_id
            return jsonify({
                'result': 'failure',
                'message': 'Invalid game id. Please send valid game_id value.',
                'error': 'Game id value does not exist.'
            }), 405
        elif current_app.config['GAMES'][game_id].is_status_completed():
            return jsonify({
                'result': 'failure',
                'message': 'Game is already completed. No more actions allowed.',
                'error': 'Game already completed.'
            }), 408
        else:
            # Retrieve the game instance
            g = current_app.config['GAMES'][game_id]
            penalty_points = g.auto_solve()

            # Save active games to JSON file for recovery after restart
            save_games_to_json()

            # Create response we are going to send back to frontend
            # Serialize crossword using CrosswordSchema
            return jsonify({
                'result': 'success',
                'message': 'Game Over - Auto Solved!',
                'crossword': CrosswordSchema.dump_solved(g.get_crossword()),
                'game_state': GameSchema.dump_state(g),
                'penalty_points': penalty_points,
            }), 200
    except Exception as e:
        return jsonify({
            'result': 'failure',
            'message': 'Error auto solve the game',
            'error': str(e)
        }), 500


@game_bp.route('/game_status/<int:game_id>', methods=['GET'])
def game_status(game_id):
    try:
        if game_id not in current_app.config['GAMES']:
            # Invalid game_id so cannot fetch status
            return jsonify({
                'result': 'failure',
                'message': 'Invalid game id. Please send valid game_id value.',
                'error': 'Game id value does not exist.'
            }), 405
        else:
            # Retrieve the game instance
            g = current_app.config['GAMES'][game_id]
            # Create response we are going to send back to frontend
            return jsonify({
                'game_id': game_id,
                'game_state': GameSchema.dump_state(g),
            }), 200
    except Exception as e:
        return jsonify({
            'result': 'failure',
            'message': 'Error fetching game status',
            'error': str(e)
        }), 500


@game_bp.route('/list_active_games/<int:user_id>', methods=['GET'])
def list_active_games(user_id):
    try:
        # Check if user is known
        if user_id == -1 or user_id not in current_app.config['USERS']:
            # Unknown user, cannot start game
            return jsonify({
                'result': 'failure',
                'message': 'Unknown user. Please log in to start a game.',
                'error': 'Unknown User ID has been received.'
            }), 400
        else:
            active_games = []
            for game_id, game in current_app.config['GAMES'].items():
                if game.user_id == user_id and not game.is_status_completed():
                    active_games.append({
                        'game_id': game_id,
                        'game_state': GameSchema.dump_state(game),
                    })

            return jsonify({
                'result': 'success',
                'message': f'Found {len(active_games)} active games for user.',
                'active_games': active_games,
            }), 200
    except Exception as e:
        return jsonify({
            'result': 'failure',
            'message': 'Error listing active games',
            'error': str(e)
        }), 500