from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def home():
    return 'Welcome to Dance Schedule App!'

if __name__ == '__main__':
    app.run()
