# Core Library
import os
from pathlib import Path

# Third party
from dotenv import load_dotenv
from werkzeug.serving import run_simple

# First party
from app.app import App

dotenv_path = Path(__file__).parent.parent / ".env.local"
load_dotenv(dotenv_path)

# CONSTANTS
DEBUG = os.getenv('DEBUG')

application = App()
run_simple('127.0.0.1', 5000, application, use_debugger=DEBUG, use_reloader=True)
