from flask import jsonify, render_template

# check api status
def api_status():
    """Return a JSON"""
    return jsonify({"status": "OK"})
    
#render landing page
def index():
    return render_template('landing.html')

#render sign-up page
def signup():
    return render_template('signup.html')

#render login page
def signin():
    return render_template('login.html')