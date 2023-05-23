from boggle import Boggle
from flask import Flask, request, render_template, session

app = Flask(__name__)
app.config["SECRET_KEY"] = "secretSauce"

boggle_game = Boggle()


@app.route("/")
def display_homepage():
    board = boggle_game.make_board()

    return render_template("index.html", board=board)
