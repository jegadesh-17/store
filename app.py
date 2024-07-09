from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')
db = client['store']  # Replace 'your_database_name' with your actual database name

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/dashboard', methods=['POST'])
def dashboard():
    username = request.form['username']
    password = request.form['password']
    # Check username and password (you would typically validate against a database here)
    # For demo purposes, let's assume username and password are correct
    return render_template('dashboard.html')

@app.route('/save_data', methods=['POST'])
def save_data():
    name = request.form['name']
    amount = request.form['amount']
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    current_date = now.strftime("%Y-%m-%d")
    data = {
        'name': name,
        'amount': amount,
        'time': current_time,
        'date': current_date
    }
    db.data_collection.insert_one(data)  # Insert data into MongoDB collection
    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    app.run(debug=True)
