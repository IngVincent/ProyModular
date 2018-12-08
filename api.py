# Flask
from flask import Flask
from flask_cors import CORS
from flask_restful import Api

# Resources
from user import User

# Flask Application and API
app = Flask(__name__)
api = Api(app, prefix='/api')

# Access-Control-Allow-Origin
CORS(app)

# Adding Resources
api.add_resource(User, '/user')

if __name__ == "__main__":
    app.run(debug=True)