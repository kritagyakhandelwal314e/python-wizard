from flask import Flask
from flask.helpers import send_file
from flask.templating import render_template
app = Flask(__name__)
print(__name__)

@app.route("/<username>/<int:post_id>")
def root(username=None, post_id=0):
  return render_template('index.html', name=username, post_id=post_id)


@app.route("/blog")
def blog():
  return 'Blogs'

@app.route("/blog/2020/dogs")
def blog2():
  return 'Dogs'

@app.route("/about")
def about():
  return render_template('about.html')