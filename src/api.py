from flask import Flask, request, jsonify
from chatbot import get_answer

app = Flask(__name__)

@app.route('/ask', methods=['POST'])
def ask():
    """API endpoint to answer user questions."""
    data = request.get_json()
    query = data['query']
    answer = get_answer(query)
    return jsonify({'answer': answer})


if __name__ == '__main__':
    app.run(debug=True)