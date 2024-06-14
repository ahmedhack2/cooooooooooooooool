from flask import Flask
from resources import ns
from flask_restx import Api

api = Api()
app = Flask(__name__)
api.init_app(app)
api.add_namespace(ns)
if __name__ == "__main__":
    app.run(debug=True)