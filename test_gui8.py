from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)


@app.route("/")
def menu():
    return """
    <h1>Main Menu</h1>
    <ul>
        <li><a href="/swchronicles">SW Chronicles</a></li>
        <li><a href="/yonder">Yonder</a></li>
    </ul>
    """


@app.route("/swchronicles")
def accordion_example():
    return render_template("swchronicles.html")


@app.route("/yonder")
def other_example():
    return render_template("yonder.html")


@socketio.on("submit")
def process_input(input_text):
    # Perform some processing on the input text
    output_text = "You entered: " + input_text
    emit("output", output_text)


if __name__ == "__main__":
    socketio.run(app)
