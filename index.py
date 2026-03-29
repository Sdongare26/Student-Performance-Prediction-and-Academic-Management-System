import sys
import os

# Add project root to path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

# Import your Flask app
from app import app

# Vercel uses this variable
# DO NOT rename 'app'