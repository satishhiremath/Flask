from flask import Flask

app = Flask(__name__)

@app.route('/only_get', methods=['GET'])
def get_only():
    return "You can only GET this webpage"

'''
# This throws error: Method Not Allowed
# The method is not allowed for the requested URL

@app.route('/only_get', methods=['POST'])
def get_only():
    return "You can only GET this webpage"
'''

if __name__ == "__main__":
    app.run(debug=True)
