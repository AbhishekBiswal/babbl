import os

from flask import Flask, request, Response
from flask import render_template, url_for, redirect, send_from_directory

from models import db, Posts, Rooms, Comments

from babbl import app

# app controllers
@app.route('/')
def index():
	return render_template('index.html')

@app.route('/<slug>')
def home(slug):
	room = Rooms.query.filter_by(slug=slug).first()
	if room is None:
		return "404. Room doesn't Exist"
	return render_template('home.html', pageTitle="Home", slug=slug, room=room, db=db, Posts=Posts, Rooms=Rooms)

@app.route('/new/<id>/<to>')
def new(id, to):
	to = "/"+to
	return render_template('new.html', pageTitle="New Post", id=id, to=to)

@app.route('/new/sub', methods=['POST'])
def newSub():
	type = request.form["post"]
	id = request.form["id"]
	ip = request.remote_addr
	if type == "short":
		content = request.form["content"]
		color = request.form["color"].lower()
		if content is None:
			return redirect("/new")
		if len(content) <= 5:
			return "Insufficient Content. Go <a href='/new'>Back</a>"
		newPost = Posts("short", "", content, ip, id, color)
		db.session.add(newPost)
		db.session.commit()
		getId = Posts.query.filter_by(post_content=content, ip=ip).first()
		if getId is None:
			return "Error. Please Try again"
		return redirect("/p/"+str(getId.id))
	return 0

@app.route('/p/<id>')
def postPage(id):
	post = Posts.query.filter_by(id=id).first()
	room = Rooms.query.filter_by(id=post.room).first()
	return render_template("post.html", post=post, db=db, Rooms=Rooms, Posts=Posts, Comments=Comments, room=room)

@app.route("/p/comment", methods=['POST'])
def comment():
	comment = request.form['comment']
	pid = request.form['pid']
	if pid is None:
		return "error"
	if len(comment) == 0:
		return "Comment too short"
	newComment = Comments(comment, pid)
	post = Posts.query.filter_by(id=pid).first()
	post.comments = post.comments + 1
	db.session.add(newComment)
	db.session.commit()
	return redirect("/p/"+str(pid))

# special file handlers
@app.route('/favicon.ico')
def favicon():
	return send_from_directory(os.path.join(app.root_path, 'static'), 'img/favicon.ico')

# error handlers
@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404
