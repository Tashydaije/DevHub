from api.v1 import db
from models.user import User
from flask import jsonify, make_response, request
import sqlalchemy
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

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
        users = User.query.all()
        return make_response(jsonify([user.json() for user in users]), 200)
    except Exception as e:
        return make_response(jsonify({'message': f'Internal server error{str(e)}'}), 500)
    
# get a user
def get_user(id):
    try:
        user = User.query.filter_by(id=id).first()
        if user:
            return make_response(jsonify({'user': user.json()}), 200)
        return make_response(jsonify({'message': 'User not found'}), 404)
    except Exception as e:
        return make_response(jsonify({'message': f'Error getting user{str(e)}'}), 500)

# update a user
def update_user(id):
    try:
        user = User.query.filter_by(id=id).first()
        if user:
            data = request.get_json()
            user.first_name = data['first_name']
            user.last_name = data['last_name']
            user.username = data['username']
            user.email = data['email']
            user.password = data['password']
            db.session.commit()
            return make_response(jsonify({'message': 'User updated successfully'}), 200)
        return make_response(jsonify({'message': 'User not found'}), 404)
    except Exception:
        return make_response(jsonify({'message': 'Error updating user'}), 500)
    
# delete a user
def delete_user(id):
    try:
        user = User.query.filter_by(id=id).first()
        if user:
            db.session.delete(user)
            db.session.commit()
            return make_response(jsonify({'message': 'User deleted successfully'}), 200)
        return make_response(jsonify({'message': 'User not found'}), 404)
    except Exception:
        return make_response(jsonify({'message': 'Error deleting user'}), 500)