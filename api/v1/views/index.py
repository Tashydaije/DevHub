from flask import jsonify

# check api status
def api_status():
    """Return a JSON"""
    return jsonify({"status": "OK"})
    