# quick prototype Flask app
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({"service": "kcl-api-project", "status": "alpha"})

@app.route('/health')
def health():
    return "OK", 200

# small endpoint used in testing
@app.route('/echo', methods=['POST'])
def echo():
    payload = request.get_json(force=True) or {}
    return jsonify({"echo": payload})

if __name__ == '__main__':
    app.run(debug=True)
