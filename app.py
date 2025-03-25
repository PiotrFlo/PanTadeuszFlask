from flask import Flask
app = Flask(name)

@app.route("/")
def index():
    return "Hello World!"

@app.route("/<name>")
def hello(name):
    return f"hello {name}"

if name == "main":
    app.run()