import os
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def index():
    return "This is my homepage"

@app.route("/hello/")
@app.route("/hello/<name>")
def hello(name='Lauren'):
    # return "Hello {0}".format(name)
    return render_template('hello.html', name=name)

@app.route("/about")
def about():
    return render_template('about.html')

# No longer necessary since we are using the Flask CLI
# if __name__ == "__main__":
#     app.run(debug=True, host=os.getenv("IP", '0.0.0.0'), port=int(os.getenv("PORT", 8080)))
