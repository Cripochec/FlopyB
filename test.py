from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api()

res = {"name": "Ivan", "sourname": "Ivanov", "number": "88007894541"}


class dd(Resource):
    def get(self):
        return res


api.add_resource(dd, "/api/dd")
api.init_app(app)

if __name__ == '__main__':
    app.run(debug=True, port=3000, host="127.0.0.1")
