from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import time
import os
import webbrowser
import threading
from chatbot import Chat

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend requests

# Serve index.html at root using render_template
@app.route('/')
def serve_index():
    return render_template('index.html')

# Chat API endpoint
@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        ch = Chat()
        data = request.get_json()
        if not data or 'prompt' not in data:
            return jsonify({'error': 'No prompt provided'}), 400
        
        user_prompt = data['prompt']
        
        # Simulate processing delay (replace with AI model call)
        time.sleep(1)
        
        # Placeholder response
        response = ch.bot(user_prompt)
        
        return jsonify({'response': response}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def open_browser():
    """Open the default browser to the app's URL after a short delay."""
    time.sleep(1)  # Wait for server to start
    webbrowser.open('http://localhost:5050')

if __name__ == '__main__':
    # Ensure index.html exists in the templates folder
    templates_dir = os.path.join(app.root_path, 'templates')
    if not os.path.exists(os.path.join(templates_dir, 'index.html')):
        print("Error: index.html not found in the templates folder.")
    else:
        # Start browser in a separate thread
        threading.Thread(target=open_browser, daemon=True).start()
        # Run Flask server
        app.run(debug=True, host='0.0.0.0', port=5050)