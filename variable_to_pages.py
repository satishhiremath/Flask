from flask import Flask

app = Flask(__name__)

@app.route('/<string:name>') #Passing name to return function
def hello_name(name):
    return "Hello " + name + ". You are on page " + name


if __name__ == "__main__":
    app.run(debug=True)
