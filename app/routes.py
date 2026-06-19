from flask import Blueprint, jsonify
import os

main = Blueprint("main", __name__)

@main.route("/")
def home():
    return jsonify({
        "message": "AutoDeploy is running 🚀"
    })

@main.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    }), 200

@main.route("/version")
def version():
    return jsonify({
        "version": os.getenv("APP_VERSION", "dev")
    })