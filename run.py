from app import create_app
import os

if __name__ == '__main__':
    current_folder = os.path.dirname(os.path.abspath(__file__))
    print("Current folder:", current_folder)
    print("Creating Flask backend app...")
    app = create_app(current_folder)
    print("Starting Flask backend server...")
    app.run(host='0.0.0.0', port=5000, debug=False)


