# ***********************************************
# TO RUN
# terminal: python -m flask run
# browser: http://http://127.0.0.1:5000/
#
# ***********************************************

from flask import Flask


app = Flask(__name__)


@app.route("/")  # when URL "/" is accesed run what is below
def hello_world():
    return "Hello, flask"


# make a flask running
if __name__ == "__main__":

    # host 0.0.0.0 is for local
    app.run(host='0.0.0.0', port=80, debug=True)
