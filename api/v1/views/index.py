from flask import jsonify
from api.v1.views import app_views

@app_views.route("/status")
def api_status():
    """Return a JSON"""
    return jsonify({"status": "OK"})