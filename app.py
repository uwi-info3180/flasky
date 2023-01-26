import os
from flask import Flask, render_template, url_for
app = Flask(__name__)


@app.route("/")
def index():
    return "This is my homepage"

@app.route("/hello/<some_name>")
def hello(some_name='John Doe'):
    # return "Hello {0}".format(some_name)
    return render_template('hello.html', name=some_name)

@app.route("/about")
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True, host=os.getenv("IP", '0.0.0.0'), port=int(os.getenv("PORT", 8080)))
