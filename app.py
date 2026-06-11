from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=['POST'])
def register():

    name = request.form['name']

    # Connect to database
    conn = sqlite3.connect('college.db')

    cursor = conn.cursor()

    # Insert data
    cursor.execute(
        "INSERT INTO students(name) VALUES (?)",
        (name,)
    )

    conn.commit()

    conn.close()

    return f"{name} added successfully"

if __name__ == '__main__':
    app.run(debug=True)