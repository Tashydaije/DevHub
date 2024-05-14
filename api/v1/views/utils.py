import requests
from flask import make_response, jsonify, session
from config import Config
import json

class OAuth2Client:
    # helper methods for handling OAuth2 authorization flows with different platforms
    def __init__(self, base_url):
        self.base_url = base_url

    def get_authorization_url(self):
        try:
            platform_params = {
                'github': {
                    'url': 'https://github.com/login/oauth/authorize',
                    'params': {
                        'client_id': Config.GITHUB_CLIENT_ID,
                        'redirect_uri': 'http://127.0.0.1:5000/api/v1/accounts/callback',
                        'scope': 'repo,user'
                    }
                },
                'stackoverflow': {
                    'url': 'https://stackoverflow.com/oauth/dialog',
                    'params': {
                        'client_id': Config.STACKOVERFLOW_CLIENT_ID,
                        'redirect_uri': 'http://127.0.0.1:5000/api/v1/accounts/callback',
                        'scope': 'read,no_expiry'
                    }
                }
            }
            platform_name = session.get('platform_name')
            print(platform_name)
            if not platform_name:
                return make_response(jsonify({'error': 'Missing platform information'}), 400)
            platform_config = platform_params.get(platform_name)
            if not platform_config:
                return make_response(jsonify({'error': 'Invalid platform'}), 400)
            url = platform_config['url']
            params = platform_config['params']

            authorization_url = f'{url}?{"&".join([f"{k}={v}" for k, v in params.items()])}'
            data = {'authorization_url': authorization_url}
            print(data)
            return data
        except Exception as e:
            return make_response(jsonify({'error': f'Failed to get authorization url: {e}'}), 500)

    def exchange_authorization_code(self, code, redirect_uri):
        try:
            platform_params = {
                'github': {
                    'url': 'https://github.com/login/oauth/access_token',
                    'data': {
                        'client_id': Config.GITHUB_CLIENT_ID,
                        'client_secret': Config.GITHUB_CLIENT_SECRET,
                        'code': code,
                        'redirect_uri': redirect_uri,
                    }
                },
                'stackoverflow': {
                    'url': 'https://stackoverflow.com/oauth/access_token',
                    'data': {
                        'client_id': Config.STACKOVERFLOW_CLIENT_ID,
                        'client_secret': Config.STACKOVERFLOW_CLIENT_SECRET,
                        'code': code,
                        'redirect_uri': redirect_uri,
                    }
                }
            }

            platform_name = session.get('platform_name')
            if not platform_name:
                return make_response(jsonify({'error': 'Missing platform information'}), 400)
            
            platform_config = platform_params.get(platform_name)
            print(platform_config)
            if not platform_config:
                return make_response(jsonify({'error': 'Invalid platform'}), 400)
            url = platform_config['url']
            data = platform_config['data']

            try:
                response = requests.post(url, data=data)
                response.raise_for_status()  # This will raise an exception for non-2xx responses

                # Manual parsing instead of using response.json()
                access_token = None
                if response.content:
                    content = response.content.decode('utf-8')  # Decode bytes to string
                    for part in content.split('&'):
                        key, value = part.split('=')
                        if key == 'access_token':
                            access_token = value.strip("'")  # Remove single quotes from value
                            break  # Stop iterating after finding access_token
                    return access_token

            except requests.exceptions.RequestException as e:
                print("Request failed:", e)
                return None
        except Exception as e:
            return make_response(jsonify({'error': f'Failed to exchange authorization code: {e}'}), 500)