from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    # context = {
    #     "title" : "Йога-центр \"Гармония\""
    # }
    return render_template("home.html") #**context)

@app.route("/about/")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run()