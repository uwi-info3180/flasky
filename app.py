import os
from flask import Flask, render_template, url_for
app = Flask(__name__)


@app.route("/")
@app.route("/<some_name>")
def hello(some_name='person'):
    return "Hello {0}".format(some_name)
    # return render_template('hello.html', name=some_name)


if __name__ == "__main__":
    app.run(debug=True, host=os.getenv("IP", '0.0.0.0'), port=int(os.getenv("PORT", 8080)))
