import sqlite3
from pathlib import Path
import bcrypt

DB_PATH = "users.db"

def init_db():
    if not Path(DB_PATH).exists():
        with sqlite3.connect(DB_PATH) as conn:
            conn.execute("""
                CREATE TABLE users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    password_hash TEXT NOT NULL
                )
            """)
            # 테스트 계정 추가: admin / password123
            pw_hash = bcrypt.hashpw("password123".encode(), bcrypt.gensalt()).decode()
            conn.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)", ("admin", pw_hash))
            conn.commit()

def get_user(username):
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.execute("SELECT id, username, password_hash FROM users WHERE username = ?", (username,))
        return cur.fetchone()
