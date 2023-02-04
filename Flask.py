from flask import Flask

app = Flask(__name__)

@app.route("http://13.40.199.5000/")
def hello():
    return "I AM A DEVOPS ENGINEER!"

if __name__ == "__main__":
    app.run()
