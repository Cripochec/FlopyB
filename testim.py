from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api', methods=['POST'])
def process_api_request():
    try:
        data = request.get_json()
        received_message = data['message']

        # Здесь вы можете обработать полученное сообщение по вашему усмотрению
        # В данном примере мы просто отправляем обратно то же самое сообщение

        response_data = {'message': received_message}
        return jsonify(response_data)

    except Exception as e:
        print(str(e))
        return jsonify({'error': 'Something went wrong'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
