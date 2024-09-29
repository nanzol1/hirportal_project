import unittest
from models import Categories, Menus, News
from scripts import app
from flask import json
from models import db

class TestPage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = app.test_client()
        cls.app.testing = True


    @classmethod
    def setUpClass(cls):
        cls.app = app.test_client()
        cls.app.testing = True

    def test_home(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code,200)

    def test_admin(self):
        response = self.app.get('/admin')
        self.assertEqual(response.status_code,200)

    def test_list_news(self):
        response = self.app.get('/admin')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Teszt', response.data)

    def test_add_news(self):
        response = self.app.post('/admin/add_news', data={
            'title': 'Teszt hír',
            'content': 'Teszt content',
            'author': 'Teszt author'
        })
        self.assertEqual(response.status_code, 302)
        with app.app_context():
            new_news = News.query.filter_by(title='Teszt hír').first()
            self.assertIsNotNone(new_news)
        
            db.session.delete(new_news)
            db.session.commit()


    def test_remove_news(self):
        with app.app_context():
            news_to_remove = News(title="Teszt hír", content="Teszt content", author="Teszt author")
            db.session.add(news_to_remove)
            db.session.commit()
            news_id = news_to_remove.id

        response = self.app.post('/admin/remove_news', data={'news_id': news_id})
        self.assertEqual(response.status_code, 302)
        with app.app_context():
            removed_news = News.query.get(news_id)
            self.assertIsNone(removed_news)


if __name__ == '__main__':
    unittest.main()