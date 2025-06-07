from flask import Flask, request, jsonify
from rebound_logic import compute_rebound_assessment

app = Flask(__name__)

@app.route("/api/rebound", methods=["POST"])
def api():
    data = request.get_json()
    result = compute_rebound_assessment(data)
    return jsonify(result)

@app.route("/")
def index():
    return "<h2>Rebound Assessment API</h2><p>Use POST /api/rebound</p>"

if __name__ == "__main__":
    app.run(debug=True)
