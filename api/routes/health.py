from flask import Blueprint, Response, request, jsonify

health = Blueprint("health", __name__)

@health.route("/")
def status():
    print("OK")
    return jsonify({"status" : "ok", "code" : 200})