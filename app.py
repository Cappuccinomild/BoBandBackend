from flask import Flask
from flask_cors import CORS
from api.auth import auth_bp
from core.database import init_db

app = Flask(__name__)
app.config.from_object("config")
CORS(app)

app.register_blueprint(auth_bp, url_prefix="/api/auth")

init_db()  # 최초 실행 시 DB 생성

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
