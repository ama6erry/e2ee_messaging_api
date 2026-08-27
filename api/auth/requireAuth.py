from functools import wraps
from flask import request, g, jsonify

from api.sessions.store import get_session


def require_auth(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        auth_header = request.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Bearer "):
            return jsonify(error="Missing or malformed Authorization header"), 401

        token = auth_header[len("Bearer "):].strip()
        if not token:
            return jsonify(error="Empty token"), 401

        session = get_session(token)
        if session is None:
            return jsonify(error="Invalid or expired session"), 401

        g.session = session
        return fn(*args, **kwargs)

    return wrapper