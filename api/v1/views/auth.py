from flask import make_response, jsonify, request
from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt_identity
from models.user import User
from api.v1 import db

# Login User
def login():
    try:
        username = request.json.get('username')
        password = request.json.get('password')

        if not username or not password:
            return make_response(jsonify({'message': 'Missing username or password'}), 400)
        
        current_user = db.session.query(User).filter_by(username=username).first()
        if not current_user or not current_user.verify_password(password):
            return make_response(jsonify({'message': 'Invalid Credentials: Password or Email'}), 401)
        
        access_token = create_access_token(identity=current_user.id)
        refresh_token = create_refresh_token(identity=current_user.id)

        return make_response(jsonify({'access_token': access_token, 'refresh_token': refresh_token}), 200)
    except Exception as e:
        return make_response(jsonify({'message': f'Internal server error {str(e)}'}), 500)

# refresh access token
def refresh():
    refresh_token = request.json.get('refresh_token')

    if not refresh_token:
        return make_response(jsonify({'message': 'Missing refresh token'}), 400)
    
    try:
        current_user_id = get_jwt_identity(refresh_token)['identity']
        access_token = create_access_token(identity=current_user_id)
        return make_response(jsonify({'access_token': access_token}), 200)
    except Exception as e:
        return make_response(jsonify({'message': f'Internal server error {str(e)}'}), 500)