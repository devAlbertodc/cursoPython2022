from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/servicios")
def servicios():
    return render_template("base.html")

@app.route("/contacto")
def contacto():
    return render_template("base.html")

@app.route("/admin")
def admin():
    return render_template("base.html")