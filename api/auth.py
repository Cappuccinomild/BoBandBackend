from flask import Blueprint, request, jsonify
from utils import generate_token

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    # 예시: 하드코딩된 사용자 검증
    if username == "admin" and password == "password123":
        token = generate_token(username)
        return jsonify({"token": token})

    return jsonify({"message": "인증 실패"}), 401
