from flask import Flask, render_template, request
from database.pgsql_connection import execute_command

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/chat", methods=['POST'])
def get_bot_response():
    query = request.json['message']
    print(request.json)
    answer = execute_command(query)
    response = {'reply': answer}
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0")
