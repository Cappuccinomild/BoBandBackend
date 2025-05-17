from flask import Blueprint, request, jsonify
from models import User
from core.utils import generate_token
import bcrypt

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    user = User.query.filter_by(username=username).first()
    if not user or not bcrypt.checkpw(password.encode(), user.password_hash.encode()):
        return jsonify({"message": "아이디 또는 비밀번호가 잘못되었습니다"}), 401

    token = generate_token(user.username)
    return jsonify({"token": token})
