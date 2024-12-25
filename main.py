from flask import Flask, render_template
import requests

app=Flask(__name__)


blog_url = "https://api.npoint.io/674f5423f73deab1e9a7"
blogResponse = requests.get(blog_url)
all_posts = blogResponse.json()


@app.route("/")
def home():
    return render_template("index.html", posts=all_posts)

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')


@app.route("/post/<int:index>")
def show_post(index):
    for each_post in all_posts:
        if each_post['id'] == index:
            return render_template("post.html", post= each_post)
    return False


if __name__=='__main__':
    app.run(debug=True)