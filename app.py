from googletrans import Translator
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
translator = Translator()

@app.route('/')
def home():
    return "🗣️ English → Telugu Translator API is running!"

@app.route('/translate', methods=['POST'])
def translate_text():
    data = request.get_json()
    text = data.get('text', '')
    if not text.strip():
        return jsonify({"translation": "దయచేసి అనువదించవలసిన వాక్యం ఇవ్వండి."})
    result = translator.translate(text, src='en', dest='te')
    return jsonify({"translation": result.text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
