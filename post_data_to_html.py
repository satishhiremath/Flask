from flask import Flask, render_template

app = Flask(__name__)

post_data = [
    {
        'title': 'Post1',
        'content': 'This is Post1 content',
        'author': 'Satish'
    },
    {
        'title': 'Post2',
        'content': 'This is Post2 content'
    }
]

@app.route('/post')
def get_only():
    return render_template("post.html", posts=post_data)

if __name__ == "__main__":
    app.run(debug=True)
