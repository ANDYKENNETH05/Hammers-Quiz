from flask import Flask, render_template, request, url_for, flash
from werkzeug.utils import redirect

app = Flask(__name__)
app.config["SECRET_KEY"] = "quiz hammer"


@app.route("/")
def index():
    return render_template("base.html")


if __name__ =='__main__':
    app.run(debug=True)