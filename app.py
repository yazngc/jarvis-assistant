from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, this is your Flask app!"

@app.route('/listen', methods=['POST'])
def listen():
    data = request.get_json()
    # Implement speech recognition and task handling logic here
    return jsonify({"message": "Processing your request"})

if __name__ == '__main__':
    app.run(debug=True)
