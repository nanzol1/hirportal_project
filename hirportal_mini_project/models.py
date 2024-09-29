from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class News(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(255),nullable=False)
    content = db.Column(db.Text,nullable=False)
    author = db.Column(db.String(255),nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.now())
    category = db.Column(db.Integer ,db.ForeignKey("categories.id"))

    def __repr__(self):
        return f'{self.title}'
    
class Menus(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(255),nullable=False)
    url = db.Column(db.String(255),nullable=False)

    def __repr__(self) -> str:
        return f'{self.name}'

class Categories(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(255) , nullable=False)
    article_id = db.Column(db.Integer ,db.ForeignKey("news.id")) 

    def __repr__(self) -> str:
        return f'{self.name}'

