from flask import Blueprint

# 각 블루프린트 import 및 prefix 등록
def register_blueprints(app):
    from .auth import auth_bp
    from .schedule import schedule_bp

    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(schedule_bp, url_prefix="/api/schedule")
