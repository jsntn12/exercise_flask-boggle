from boggle import Boggle
from flask import Flask, request, render_template, session, jsonify

app = Flask(__name__)
app.config["SECRET_KEY"] = "secretSauce"

boggle_game = Boggle()


@app.route("/")
def display_homepage():
    board = boggle_game.make_board()
    session["board"] = board

    return render_template("index.html", board=board)


@app.route("/check-word")
def word_check():
    word = request.args["word"]
    board = session["board"]
    verify_word = boggle_game.check_valid_word(board, word)

    return jsonify({"result": verify_word})
