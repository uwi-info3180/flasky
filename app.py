import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
@app.route("/<myname>")
def hello(myname='person'):
    return "Hello {0}".format(myname)

if __name__ == "__main__":
    app.run(host=os.getenv("IP",'0.0.0.0'),
    port=int(os.getenv("PORT", 8080)))