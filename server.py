from sqlite3 import Connection as SQLite3Connection
from datetime import datetime
from sqlalchemy import event
from sqlalchemy.engine import Engine
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import linked_list,Hashed_table, binarysearchtree, custom_q, custom_stack
import random

# app
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sqlitedb.file"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = 0

# configure sqlite3 to enforce foreign key contraints
@event.listens_for(Engine, "connect")
def _set_sqlite_pragma(dbapi_connection, connection_record):
    if isinstance(dbapi_connection, SQLite3Connection):
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON;")
        cursor.close()


db = SQLAlchemy(app)
now = datetime.now()

# models
class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))
    address = db.Column(db.String(200))
    phone = db.Column(db.String(50))
    posts = db.relationship("BlogPost", cascade="all, delete")

class BlogPost(db.Model):
    __tablename__ = "blog_post"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    body = db.Column(db.String(200))
    date = db.Column(db.Date)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

# routes
@app.route("/user", methods=["POST"])
def create_user():
    data = request.get_json()
    new_user = User(      # ****TODO: how to get data['name'] from UI input?
        name=data["name"],
        email=data["email"],
        address=data["address"],
        phone=data["phone"],
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User created"}), 200

'''-----------------------------------------------------------------------------------
    *** Use LinkedList to connect all Users with ID in ascending/descending order ***
    _____________________________________________________________________________    '''
@app.route("/user/descending_id", methods=["GET"])
def get_all_users_descending():
    users = User.query.all()
    all_users_ll = linked_list.LinkedList()

    for user in users:
        all_users_ll.insert_beginning(
            {
                "id": user.id,
                "name": user.name,
                "email": user.email,
                "address": user.address,
                "phone": user.phone,
            }
        )

    return jsonify(all_users_ll.to_list()), 200


@app.route("/user/ascending_id", methods=["GET"])
def get_all_users_ascending():
    users = User.query.all()
    all_users_ll = linked_list.LinkedList()

    for user in users:
        all_users_ll.insert_at_end(
            {
                "id": user.id,
                "name": user.name,
                "email": user.email,
                "address": user.address,
                "phone": user.phone,
            }
        )

    return jsonify(all_users_ll.to_list()), 200


@app.route("/user/<user_id>", methods=["GET"])
def get_one_user(user_id):
    users = User.query.all()
    all_users_ll = linked_list.LinkedList()

    for user in users:
        all_users_ll.insert_beginning(
            {
                "id": user.id,
                "name": user.name,
                "email": user.email,
                "address": user.address,
                "phone": user.phone,
            }
        )

    user = all_users_ll.get_user_by_id(user_id)

    return jsonify(user), 200


@app.route("/user/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    db.session.delete(user)
    db.session.commit()
    return jsonify({}), 200

'''-----------------------------------------------------------------------------------
            *** Use Hashed Table to create and manage Blogposts  ***
    _____________________________________________________________________________    '''

@app.route('/blog_post/<user_id>', methods=['POST'])
def create_blog_post(user_id):
    # check if user_id is existed in db
    data = request.get_json()
    user = User.query.filter_by(id=user_id).first()
    if user:
        ht = Hashed_table.HashedTable(8)
        ht.add_key_value_to_ht('title',data['title']) # TODO: how to deliver these blogpost fields data to the url server?
        ht.add_key_value_to_ht('body', data['body'])
        ht.add_key_value_to_ht('date', now)
        ht.add_key_value_to_ht('user_id', user_id)
        blog_post = BlogPost(
            title = ht.get_value_from_key('title'),
            body = ht.get_value_from_key('body'),
            date = ht.get_value_from_key('date'),
            user_id = ht.get_value_from_key('user_id')
        )
        db.session.add(blog_post)
        db.session.commit()
        return jsonify({'message': 'You have successfully created a blogpost'}), 200
    else:
        return jsonify({'message': 'The user_id is not existed.'}), 400


@app.route('/blog_post/<blog_post_id>', methods=['GET'])
def get_one_blog_post(blog_post_id):
    bst = binarysearchtree.BinarySearchTree()
    blogposts = BlogPost.query.all()
    random.shuffle(blogposts)
    for bg in blogposts:
        bst.insert_node({
            "title": bg.title,
            "body": bg.body,
            "id": bg.id,
            "date": bg.date,
            "user_id":bg.user_id
        })

    post = bst.search(blog_post_id)
    if not post:
        return jsonify({"message":"This blogpost id is not existed."}), 400
    else:
        return jsonify(post), 200

@app.route('/blog_post/numeric_body', methods=['GET'])
def get_blogs_numeric_body():
    posts = BlogPost.query.all()
    que = custom_q.Custom_Q()
    for p in posts:
        que.enqueue(p)
    numeric_posts = []
    for p in range(len(posts)):
        post = que.dequeue()
        numeric_body = 0
        for char in post.body:
            numeric_body += ord(char)
        numeric_posts.append(
            {
                "id":post.id,
                "title": post.title,
                "body" : numeric_body,
                "user_id" : post.user_id
            }
        )

    return jsonify(numeric_posts), 200

@app.route('/blog_post/remove_last_10', methods=['DELETE'])
def remove_last_10_posts():
    posts = BlogPost.query.all()
    s = custom_stack.Stack()
    for p in posts:
        s.push(p)
    removed_posts=[]
    for _ in range(10):
        post = s.pop()
        # removed_posts.append({
        #     "id" : post.id,
        #     "title": post.title,
        #     "user_id" : post.user_id,
        #     "body": post.body[:100]
        # })
        db.session.delete(post)
        db.session.commit()

    return jsonify({"message": "success"}), 200


if __name__ == '__main__':
    app.run(debug=True)
