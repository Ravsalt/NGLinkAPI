# app.py
from flask import Flask, request, jsonify
from ngl_api_client import submit_to_ngl
import logging

# Set up logging: Logs will be written to logs/app.log
logging.basicConfig(filename='logs/app.log', level=logging.DEBUG)

app = Flask(__name__)

@app.route('/api/submit', methods=['POST'])
def submit_to_ngl_endpoint():
    username = request.form.get('username')
    question = request.form.get('question')
    device_id = request.form.get('deviceId')
    game_slug = request.form.get('gameSlug', '')
    referrer = request.form.get('referrer', '')

    logging.info(f"Received submission from {username}: {question}")
    response = submit_to_ngl(username, question, device_id, game_slug, referrer)
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
