from flask import Flask


app = Flask(__name__)

# Buttercup automation automates lights, thermostats, door locks and other
# periperal devices in Buttercup.


@app.route("/")
def hello():
    return "Hello Buttercup!"

if __name__ == "__main__":
    app.run()
