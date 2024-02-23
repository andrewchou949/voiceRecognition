from flask import Flask, request, jsonify #pip install flask
from flask_cors import CORS #pip install flask-cors
from transcribe import transcribe_audio, generate_summary
from dotenv import load_dotenv
import os

app = Flask(__name__)
CORS(app)
#CORS(app, resources={r"/upload": {"origins": "http://localhost:3000"}})

@app.route('/')
def hello():
    return "Hello, World"

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file:
        try:
            transcription = transcribe_audio(file)
            return jsonify({'transcription': transcription}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500

@app.route('/summarize', methods=['POST'])
def summarize_text():
    data = request.get_json()  # Get data sent from the frontend
    text_to_summarize = data.get('text', '')
    
    # Ensure there's text to summarize
    if not text_to_summarize:
        return jsonify({'error': 'No text provided'}), 400

    summary = generate_summary(text_to_summarize)
    if summary:
        return jsonify({'summary': summary}), 200
    else:
        return jsonify({'error': 'Failed to generate summary'}), 500

# For debug mode
if __name__ == '__main__':
    # app.debug = True
    app.run(port=int(os.environ.get("PORT", 8080)),host='0.0.0.0',debug=True)

# if __name__ == "__main__":
#     port = int(os.environ.get("PORT", 8080))
#     app.run(debug=False, host="0.0.0.0", port=port)