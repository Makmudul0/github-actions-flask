from flask import Flask
import psycopg2
import os

app = Flask(__name__)

@app.route('/')
def home():
    try:
        conn = psycopg2.connect(
            host=os.getenv('POSTGRES_HOST'),
            database=os.getenv('POSTGRES_DB'),
            user=os.getenv('POSTGRES_USER'),
            password=os.getenv('POSTGRES_PASSWORD'),
        )
        cur = conn.cursor()
        cur.execute('SELECT version();')
        db_version = cur.fetchone()
        return f"Connected to PostgreSQL: {db_version}"
    except Exception as e:
        return f"Database connection error: {e}"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
