from flask import Blueprint, Response, request, jsonify, g
from api.auth.requireAuth import require_auth

#status blueprint
status = Blueprint('status', __name__)


@status.route("/api/status", defaults={"name": None})
@status.route("/api/status/<name>")
def get_status(name):
    payload = {"status": "ok"}
    if name is not None:
        payload["name"] = name
    return jsonify(payload), 200



@status.route("/api/whoami")
@require_auth
def whoami():
    return jsonify(user_id=g.session.user_id), 200