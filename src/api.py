from flask import Flask, request, jsonify
from chatbot import get_answer

import json

app = Flask(__name__)

@app.route('/ask', methods=['POST'])
def ask():
    
    data = request.get_json()
    query = data['query']
    answer = get_answer(query)

    apiLog = {
        "Query": query,
        "Answer": answer
    }

    with open("api_logs.txt", "w") as f:
        json.dump(apiLog, f, indent=4)
    
    return jsonify({'answer': answer})


if __name__ == '__main__':
    app.run(debug=True)