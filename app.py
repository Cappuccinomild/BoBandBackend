from flask import Flask
from flask_cors import CORS
from api.auth import auth_bp
from models import db

app = Flask(__name__)
app.config.from_object("config")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

CORS(app)
db.init_app(app)

app.register_blueprint(auth_bp, url_prefix="/api/auth")

# DB 초기화
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
