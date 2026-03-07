from flask import Flask, request, jsonify

app = Flask(__name__)

current_string = {"value": ""}

@app.route('/update', methods=['POST'])
def update():
    data = request.json
    current_string["value"] = data["value"]
    return jsonify({"status": "ok"})

@app.route('/get', methods=['GET'])
def get():
    return jsonify(current_string)

if __name__ == '__main__':
    app.run()