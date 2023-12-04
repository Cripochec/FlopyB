from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api', methods=['POST'])
def process_data():
    data_from_client = request.data.decode('utf-8')
    processed_data = data_from_client + " hello People"
    return jsonify(result=processed_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
