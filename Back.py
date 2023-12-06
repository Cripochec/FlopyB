from flask import Flask
from flask_restful import Api, Resource, reqparse
import DB
import CONST

app = Flask(__name__)
api = Api()


class registration_acc(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("login", type=str)
        parser.add_argument("pas1", type=str)
        parser.add_argument("pas2", type=str)

        args = parser.parse_args()

        login = args.login
        pas1 = args.pas1
        pas2 = args.pas2

        con = DB.connect_db(CONST.database_name)

        if login not in DB.get_all_logins(con):
            if len(pas1) > 4 and len(pas2) > 4:
                if pas1 == pas2:
                    DB.add_new_account(con, login, pas1)
                    return "CODE1"
                else:
                    return "CODE12"
            else:
                return "CODE11"
        else:
            return "CODE10"


class login_acc(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("login", type=str)
        parser.add_argument("pas", type=str)

        args = parser.parse_args()

        login = args.login
        pas = args.pas

        con = DB.connect_db(CONST.database_name)

        result = DB.get_password_by_login(con, login)

        if result[0] == "CODE13":
            return "CODE13"
        elif pas == result[0]:
            return result[1]
        else:
            return "CODE14"


        # if id == 0:
        #     return res
        # else:
        #     return res[id]

# class dd(Resource):
#     def get(self, id):
#         if id == 0:
#             return res
#         else:
#             return res[id]
#
#     def delete(self, id):
#         del res[id]
#         return res


api.add_resource(registration_acc, "/api/registration")
api.add_resource(login_acc, "/api/login")
api.init_app(app)

if __name__ == '__main__':
    app.run(debug=True, port=5000, host="127.0.0.1")
