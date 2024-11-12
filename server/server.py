from flask import Flask, jsonify, request
from markupsafe import escape
from stateful_bot import ask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def main():
    return jsonify({"message": 'Working!!'})

@app.route('/chat/', methods=['POST'])
def chat():
    question = request.json.get('question')
    answer = ask(question)

    # return answer
    return jsonify({"answer": answer}), 201

if __name__ == "__main__":
    app.run(debug=True, port=8080)