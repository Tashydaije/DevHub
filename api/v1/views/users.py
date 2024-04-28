from api.v1 import db
from models.user import User
from flask import jsonify, make_response, request
import sqlalchemy
from sqlalchemy.exc import SQLAlchemyError

# create a user
def create_user():
    try:
        data = request.get_json()
        print(f"Received user data: {data}")
        new_user = User(first_name=data['first_name'],
                        last_name=data['last_name'],
                        username=data['username'],
                        email=data['email'],
                        password=data['password']
                    )
        print(f"Created user object: {new_user}")
        db.session.add(new_user)
        db.session.commit()
        print("User created successfully in database.")
        return make_response(jsonify({'message': 'User created successfully'}), 201)
    except sqlalchemy.exc.IntegrityError as e:  # Catch database integrity errors
        return make_response(jsonify({'message': f"Database error: {str(e)}"}), 500)
    except SQLAlchemyError as e:
        return make_response(jsonify({'message': f"Database error: {str(e)}"}), 500)
    except (KeyError, ValueError) as e:  # Catch specific exceptions
        return make_response(jsonify({'message': f"Error: {str(e)}"}), 400)  # Bad request
    except Exception as e:  # Catch general exceptions
        return make_response(jsonify({'message': f'Internal server error{str(e)}'}), 500)

# get all users
def get_users():
    try:
        print(User)
        users = db.session.query(User).all()
        return make_response(jsonify([user.json() for user in users]), 200)
    except Exception as e:
        return make_response(jsonify({'message': f'Internal server error{str(e)}'}), 500)
    
# get a user
def get_user(id):
    try:
        user = db.session.query(User).filter_by(id=id).first()
        if user:
            return make_response(jsonify({'user': user.json()}), 200)
        return make_response(jsonify({'message': 'User not found'}), 404)
    except Exception as e:
        return make_response(jsonify({'message': f'Error getting user{str(e)}'}), 500)

# update a user
def update_user(id):
    try:
        user = db.session.query(User).filter_by(id=id).first()
        if not user:
            return make_response(jsonify({'message': 'User not found'}), 404)
        data = request.get_json()
        if not data:
            return make_response(jsonify({'message': 'No data provided'}), 400)
        update_fields = {
            'first_name': data.get('first_name'),
            'last_name': data.get('last_name'),
            'username': data.get('username'),
            'email': data.get('email'),
            'password': data.get('password'),
        }
        for key, value in update_fields.items():
            if value is not None and key not in('id', 'created_at', 'updated_at'):
                setattr(user, key, value)
        db.session.commit()
        return make_response(jsonify({'message': 'User updated successfully'}), 200)
    except Exception as e:
        return make_response(jsonify({'message': f'Error updating user{str(e)}'}), 500)
    
# delete a user
def delete_user(id):
    try:
        user = db.session.query(User).filter_by(id=id).first()
        if user:
            db.session.delete(user)
            db.session.commit()
            return make_response(jsonify({'message': 'User deleted successfully'}), 200)
        return make_response(jsonify({'message': 'User not found'}), 404)
    except Exception:
        return make_response(jsonify({'message': 'Error deleting user'}), 500)