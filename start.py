import os
import sys

# Set environment variables for better compatibility
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # Reduce TensorFlow logging
os.environ['PYTHONUNBUFFERED'] = '1'

try:
    import tensorflow as tf
    print(f"TensorFlow version: {tf.__version__}")
except ImportError as e:
    print(f"TensorFlow import error: {e}")
    print("Attempting to install compatible TensorFlow version...")
    os.system(f"{sys.executable} -m pip install tensorflow")
    import tensorflow as tf

# Import and run the Flask app
from app import app

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
