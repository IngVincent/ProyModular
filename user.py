from flask import jsonify, request
from flask_restful import Resource

class User(Resource):
 
    def post(self):
        try:
            return jsonify({'success':True, 'message':'correcto'})
        except:
            return jsonify({'success':False, 'message':'correcto'})

    def put(self):
        try:
            return jsonify({'success':True, 'message':'correcto'})
        except:
            return jsonify({'success':False, 'message':'correcto'})

    def delete(self):
        try:
            return jsonify({'success':True, 'message':'correcto'})
        except:
            return jsonify({'success':False, 'message':'correcto'})

    def get(self):
        try:
            return jsonify({'success':True, 'message':'correcto'})
        except:
            return jsonify({'success':False, 'message':'correcto'})