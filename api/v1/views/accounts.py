
from flask import make_response, jsonify, request, session
from models.platform import Platform
from models.account import Account
from models.user import User
from .utils import OAuth2Client
from api.v1 import db

def connect_account():
    # connect devhub user account with their github account
    try:
        platform_data = request.get_json()

        if not platform_data:
            return make_response(jsonify({'error': 'Missing platform data'}), 400)

        platform_name = platform_data.get('platform_name')
        if not platform_name:
            return make_response(jsonify({'error': 'Platform name is required'}), 400)

        # Retrieve platform details
        platform = db.session.query(Platform).filter_by(name=platform_name).first()
        if not platform:
            return make_response(jsonify({'error': 'Platform not found'}), 404)

        # Initiate OAuth2 flow
        oauth_client = OAuth2Client(platform.api_url)
        try:
            session['platform_name'] = platform_name
            authorization_url = oauth_client.get_authorization_url()
            print(authorization_url)
            #if authorization_url.status_code != 200:
            #    error_message = authorization_url.json().get('error')
            #    return make_response(jsonify({'error': f'Error generating authorization URL- status not 200: {error_message}'}), 500)
            url_string = authorization_url['authorization_url']
        except Exception as e:
            # Handle error and return appropriate response
            return make_response(jsonify({'error': f'Error generating authorization URL: {str(e)}'}), 500)

        # Store redirect URI in session (replace with actual redirect URI)
        session['redirect_uri'] = 'http://127.0.0.1:5000/api/v1/accounts/callback'

        # Extract data from Response object
        data = {'authorization_url': url_string}
        print(data)

        return make_response(jsonify(data), 302)
    except Exception as e:
        return make_response(jsonify({'message': f'Internal server error {str(e)}'}), 500)

def handle_callback():
    try:
        code = request.args.get('code')
        print(code)
        if not code:
            return make_response(jsonify({'error': 'Missing authorization code'}), 400)

        # Retrieve redirect URI from session
        session['redirect_uri'] = 'http://127.0.0.1:5000/api/v1/accounts/callback'
        redirect_uri = session.get('redirect_uri')
        print(redirect_uri)
        if not redirect_uri:
            return make_response(jsonify({'error': 'Invalid redirect URI'}), 400)

        # Retrieve platform details
        platform_name = session.get('platform_name')
        if not platform_name:
            return make_response(jsonify({'error': 'Missing platform information'}), 400)
        print(platform_name)

        platform = db.session.query(Platform).filter_by(name=platform_name).first()
        if not platform:
            return make_response(jsonify({'error': 'Platform not found'}), 404)

        # Exchange authorization code for access token

        oauth_client = OAuth2Client(platform.api_url)
        access_token = oauth_client.exchange_authorization_code(code, redirect_uri)
        #print(access_token)

        # Create or update user account
        user_id = session.get('id')  # Replace with actual user ID from the session or authentication
        print(user_id)
        account = db.session.query(Account).filter_by(platform_id=platform.id, user_id=user_id).first()
        if not account:
            account = Account(platform_id=platform.id, user_id=user_id, access_token=access_token)
            db.session.add(account)
        else:
            account.access_token = access_token

        db.session.commit()

        return make_response(jsonify({'message': 'Account connected successfully'}), 201)
    except Exception as e:
        return make_response(jsonify({'message': f'Internal server error {str(e)}'}), 500)
