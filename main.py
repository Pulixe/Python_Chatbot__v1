from flask_cors import CORS
from flask import Flask, request
from flask_restful import Api, Resource
import chatbot
import json
import os

#dont change until the lambda AWS is ready
apikey = "000000abc1234ABC"

app = Flask(__name__)
api = Api(app)

#habilita la conexion y resuelve problemas de CORS
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


#class for serving bot api import from chatbot.py
class Bot(Resource):
    @staticmethod
    def post():
        data = request.get_json()
        if data['msg'] != " ":
            message = data['msg']
            bot = chatbot.chatbot_response(message)
            resp = {'msg': str(bot)}
            return resp , 200
        else:
            return "{'msg':'error no hay mensaje'}"

#añadir Clase a la ruta 
api.add_resource(Bot, '/api/v1/chatbot')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, threaded=True)
