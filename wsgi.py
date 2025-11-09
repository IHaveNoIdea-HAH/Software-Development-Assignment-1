from app import create_app
import os

current_folder = os.path.dirname(os.path.abspath(__file__))
# create_app expects the current folder as an argument
app = create_app(current_folder)

# Run with gunicorn (WSL / Linux / production):
# gunicorn -w 1 -b 0.0.0.0:8000 wsgi:app
#
# Windows note: gunicorn does not run natively on Windows.
# We can use WSL or Docker, or use Waitress as a Windows alternative:
# pip install waitress
# waitress-serve --listen=0.0.0.0:5000 wsgi:app
