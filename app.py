from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Flask API!"

@app.route('/api/data')
def get_data():
    data = {
        "name": "Alessandra",
        "role": "Python Developer",
        "focus": "Automation and Data Processing"
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
