from flask import Flask, redirect, render_template

app = Flask(__name__)

@app.route("/")
def no_ninjas():
    return render_template("index.html")

@app.route("/ninja")
def all_ninjas():
    return render_template("ninja.html", ninja="static/TMNT.jpg")

@app.route("/ninja/<id>")
def ninjas(id):
    if (id == "blue"):
        return render_template("ninja.html", ninja="../static/leonardo.jpeg")
    elif (id == "purple"):
        return render_template("ninja.html", ninja="../static/donatello.gif")
    elif (id == "orange"):
        return render_template("ninja.html", ninja="../static/michaelangelo.gif")
    elif (id == "red"):
        return render_template("ninja.html", ninja="../static/raphael.jpg")
    else:
        return render_template("ninja.html", ninja="../static/april.jpg")


app.run(debug=True)
