from flask import Flask, render_template
import sqlite3 as sql


DB_NAME = 'codewars_tracking.db'

app = Flask(__name__)


@app.route('/')
def home():

    with sql.connect(DB_NAME) as con:
        cur = con.cursor()
        entries = cur.execute('SELECT * FROM Players').fetchall()
        data = [
            {'name': name, 'id': user_id, 'score': curr - start}
            for (user_id, name, start, curr) in entries
        ]
        data = [
            {'rank': idx, **i}
            for idx, i in enumerate(
                sorted(data, key=lambda x: x['score'], reverse=True), 1
            )
        ]

    return render_template(
        'index.html',
        players=data
    )
