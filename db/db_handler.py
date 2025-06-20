# db_handler.py
import sqlite3
import hashlib
import os

DB_PATH = 'user_auth.db'

def hash_password(password, salt=None):
    if salt is None:
        salt = os.urandom(16)
    elif isinstance(salt, str):
        salt = bytes.fromhex(salt)
    hash_val = hashlib.sha256(salt + password.encode()).hexdigest()
    return salt.hex(), hash_val

def create_user(user_id, password):
    salt, hashed_pw = hash_password(password)
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                   id TEXT PRIMARY KEY,
                   password TEXT NOT NULL,
                   salt TEXT NOT NULL
                 )''')
    # ID 중복 확인
    c.execute("SELECT 1 FROM users WHERE id = ?", (user_id,))
    if not c.fetchone():
        c.execute("INSERT INTO users (id, password, salt) VALUES (?, ?, ?)", (user_id, hashed_pw, salt))
        print(f"[INFO] Initial admin account created: {user_id}/(hidden)")
    conn.commit()
    conn.close()

def verify_login(user_id, input_pw):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT password, salt FROM users WHERE id = ?", (user_id,))
    result = c.fetchone()
    conn.close()

    if result:
        stored_hash, stored_salt = result
        _, input_hash = hash_password(input_pw, stored_salt)
        return input_hash == stored_hash
    return False

# ✅ 최초 실행 시 admin 계정 자동 1회 생성
def init_admin_account():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                   id TEXT PRIMARY KEY,
                   password TEXT NOT NULL,
                   salt TEXT NOT NULL
                 )''')
    c.execute("SELECT COUNT(*) FROM users WHERE id = 'admin'")
    if c.fetchone()[0] == 0:
        create_user("name", "123")
    conn.close()
