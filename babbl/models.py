# Put models here

"""
import datetime
from shuffl.core import db

class User(db.DynamicDocument):
	created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
	email = db.StringField(max_length=255, required=True, unique=True)

"""

from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Posts(db.Model):
	__tablename__ = 'posts'
	id = db.Column(db.Integer, primary_key=True)
	post_type = db.Column(db.String(300))
	post_title = db.Column(db.String(300))
	post_content = db.Column(db.String(300))
	ip = db.Column(db.String(300))
	when = db.Column(db.String(300))
	room = db.Column(db.Integer)
	comments = db.Column(db.Integer)
	hidden = db.Column(db.Integer)
	color = db.Column(db.String(300))

	def __init__(self, post_type, post_title, post_content, ip, room, color):
		self.post_type = post_type
		self.post_title = post_title
		self.post_content = post_content
		self.ip = ip
		self.room = room
		self.comments = 0
		self.hidden = 0
		self.color = color

class Rooms(db.Model):
	__tablename__ = 'rooms'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(300))
	slug = db.Column(db.String(300))
	desc = db.Column(db.String(300))

	def __init__(self, name, slug, desc):
		self.name = name
		self.slug = slug
		self.desc = desc

class Comments(db.Model):
	__tablename__ = 'comments'
	id = db.Column(db.Integer, primary_key=True)
	content = db.Column(db.String(300))
	p_id = db.Column(db.Integer)
	when = db.Column(db.String(300))

	def __init__(self, content, p_id):
		self.content = content
		self.p_id = p_id