from flask import Blueprint, request, jsonify
from utils import verify_token

api_bp = Blueprint("schedule", __name__)

@api_bp.route("/api/submit", methods=["POST"])
def submit():
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        return jsonify({"message": "인증 토큰이 필요합니다"}), 401

    token = auth_header.split(" ")[1]
    username = verify_token(token)
    if not username:
        return jsonify({"message": "유효하지 않거나 만료된 토큰입니다"}), 401

    data = request.json
    print(f"[{username}] submitted: {data}")
    return jsonify({"message": "일정 저장됨"}), 200

@api_bp.route("/results", methods=["GET"])
def results():
    return jsonify({"common_times": ["13:00~14:00", "15:00~16:00"]})
