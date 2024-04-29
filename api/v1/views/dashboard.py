from flask import make_response, jsonify, request
from flask_jwt_extended import jwt_required

# get user dashboard
@jwt_required()
def dashboard():
    try:
        return make_response(jsonify({'message': 'User dashboard: Only a registered user can access'}), 200)
    except Exception as e:
        return make_response(jsonify({'message': f'Internal Server Error {str(e)}'}), 500)
    