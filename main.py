from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    context = {
        "link" : "Записаться"
    }
    return render_template("home.html", **context)

@app.route("/about/")
def about():
    context = {
        "link": "Оставить отзыв"
    }
    return render_template("about.html", **context)

if __name__ == "__main__":
    app.run()