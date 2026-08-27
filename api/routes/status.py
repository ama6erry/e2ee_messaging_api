from flask import Blueprint, Response, request, jsonify

#status blueprint
status = Blueprint('status', __name__)

# status blueprint
@status.route("/api/status", defaults={"name": None})
@status.route("/api/status/<name>")
def get_status(name):
    if name is None:
        return jsonify({"status": "ok", "code": 200})

    return jsonify({
        "status": "ok",
        "code": 200,
        "name": name
    })