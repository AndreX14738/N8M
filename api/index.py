import sys
import os

# Add the api directory to sys.path for Vercel
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app.main import app

# Vercel serverless handler
handler = app