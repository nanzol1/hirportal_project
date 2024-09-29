from datetime import datetime, timedelta
from flask import render_template, request, redirect, url_for
from scripts import app
from models import Categories, Menus, News, db


@app.route('/')
def index():
    category = request.args.get('category')
    categories = Categories.query.all()
    category_id=[]
    if category:
        news = News.query.filter_by(category=category).all()
    else:
        news = News.query.all()
    
    urls = Menus.query.all()
    return render_template('index.html',urls=urls,news=news,categories=categories,category_id=category_id)

@app.route('/admin')
def list_news():
    news = News.query.all()
    urls = Menus.query.all()
    return render_template('admin.html',news=news,urls=urls)

@app.route('/admin/add_news',methods=['POST'])
def add_news():
    title = request.form['title']
    content = request.form['content']
    author = request.form['author']

    recently = datetime.now() - timedelta(seconds=5)
    recent_news = News.query.filter_by(title=title,content=content,author=author).filter(News.timestamp > recently).first()

    if recent_news:
        return f'Ez már el lett küldve!'
    
    new_news = News(title=title,content=content,author=author)


    

    db.session.add(new_news)
    db.session.commit()

    return redirect(url_for('list_news'))

@app.route('/admin/remove_news' , methods=['POST'])
def remove_news():
    news_id = request.form['news_id']
    news_to_remove = News.query.get(news_id)

    if news_to_remove:
        db.session.delete(news_to_remove)
        db.session.commit()
        return redirect(url_for('list_news'))
    else:
        return f'A hír nem található'
    