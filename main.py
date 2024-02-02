from flask import Flask, render_template, redirect, request
import psycopg2

conn = psycopg2.connect(
    host = 'localhost',
    dbname = 'sql_demo',
    user = 'postgres',
    password = 'ianojr',
    port = 5432
)
cur = conn.cursor()

app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>Hello</h1>'

app.run(debug = True)