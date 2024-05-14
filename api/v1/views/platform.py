from api.v1 import db
from models.platform import Platform
from flask import jsonify, make_response, request

PLATFORM_API_URLS = {
    'github': 'https://api.github.com/',
    'stackoverflow': 'https://api.stackexchange.com/',
}

PLATFORM_OAUTH_URLS = {
    'github': 'https://github.com/login/oauth/access_token',
    'stackoverflow': 'https://stackoverflow.com/oauth/access_token'
}

def create_platform():
    try:    
        platform_data = request.get_json()

        if not platform_data:
            return make_response(jsonify({'error': 'Missing platform data'}), 400)

        name = platform_data.get('name')
        if not name:
            return make_response(jsonify({'error': 'Platform name is required'}), 400)

        # Check if platform already exists
        existing_platform = db.session.query(Platform).filter_by(name=name).first()
        if existing_platform:
            return make_response(jsonify({'error': 'Platform already exists'}), 409)

        # Retrieve API URL (if available)
        api_url = PLATFORM_API_URLS.get(name)
        oauth_url = PLATFORM_OAUTH_URLS.get(name)

        # Create new platform
        new_platform = Platform(name=name, api_url=api_url, oauth_url=oauth_url)
        db.session.add(new_platform)
        db.session.commit()

        return make_response(jsonify({'platform': new_platform.json()}), 201)
    except Exception as e:
        return make_response(jsonify({'message': f'Internal server error {str(e)}'}), 500)