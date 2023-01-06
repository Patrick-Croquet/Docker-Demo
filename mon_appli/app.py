import os
from flask import Flask
app = Flask(__name__)
@app.route('/')
def main():
    return "<b>Bienvenue</b>"
@app.route('/autre_chose')
def hello():
    return "<b style='color:blue;'>Il fait beau</b>"
if __name__ == "__main__":
    app.run()