from flask import Flask, json
import requests
from DataObj import DataObj

app = Flask(__name__)

data = DataObj('userId', id, 'title', 'body')


@app.route("/posts")
def get_posts():
    posts_response = requests.get('https://jsonplaceholder.typicode.com/posts')
    if posts_response.status_code != 200:
        print("too bad")

    posts = posts_response.json()
    response = app.response_class(
        response=json.dumps(posts),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route("/posts/<id>")
def get_posts_id(id):
    posts_response = requests.get('https://jsonplaceholder.typicode.com/posts/'+id)
    if posts_response.status_code != 200:
        print("too bad")

    posts = posts_response.json()
    return posts


@app.route("/posts/user/<userId>")
def get_posts_user(userId):
    posts_response = requests.get('https://jsonplaceholder.typicode.com/posts?userId='+userId)
    if posts_response.status_code != 200:
        print("too bad")

    posts = posts_response.json()
    response = app.response_class(
        response=json.dumps(posts),
        status=200,
        mimetype='application/json'
    )

    return response


@app.route("/posts/<userId>/comments")
def get_posts_user_comments(userId):
    posts_response = requests.get('https://jsonplaceholder.typicode.com/posts/' +userId + '/comments')
    if posts_response.status_code != 200:
        print("too bad")

    posts = posts_response.json()
    response = app.response_class(
        response=json.dumps(posts),
        status=200,
        mimetype='application/json'
    )

    return response

if __name__ == "__main__":
    app.run(debug=True)