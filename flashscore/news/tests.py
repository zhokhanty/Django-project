from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from news.models import News


class NewsTests(TestCase):

    def setUp(self):
        # Создание тестового пользователя
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_news_creation(self):
        # Проверка создания новости
        news = News.objects.create(
            title='Test News',
            content='This is a test news content.',
            author=self.user
        )
        # Проверка, что новость была сохранена в базе данных
        self.assertEqual(news.title, 'Test News')
        self.assertEqual(news.content, 'This is a test news content.')
        self.assertEqual(news.author, self.user)

    def test_create_news_view(self):
        self.client.login(username='testuser', password='testpassword')  # Убедись, что ты залогинен
        response = self.client.get(reverse('create_news'))
        self.assertEqual(response.status_code, 200)
        data = {'title': 'New Test News', 'content': 'This is a new test news.'}
        response = self.client.post(reverse('create_news'), data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(News.objects.count(), 1)
        self.assertEqual(News.objects.first().title, 'New Test News')

    def test_edit_news_view(self):
        news = News.objects.create(
            title='Old News',
            content='Old content',
            author=self.user
        )
        self.client.login(username='testuser', password='testpassword')  # Убедись, что ты залогинен
        response = self.client.get(reverse('edit_news', kwargs={'news_id': news.id}))
        self.assertEqual(response.status_code, 200)

        data = {'title': 'Updated News', 'content': 'Updated content of the news.'}
        response = self.client.post(reverse('edit_news', kwargs={'news_id': news.id}), data)
        self.assertEqual(response.status_code, 302)
        news.refresh_from_db()
        self.assertEqual(news.title, 'Updated News')
        self.assertEqual(news.content, 'Updated content of the news.')

    def test_access_forbidden_for_non_author(self):
        other_user = User.objects.create_user(username='otheruser', password='otherpassword')
        news = News.objects.create(
            title='News by another user',
            content='Content from another user',
            author=other_user
        )
        self.client.login(username='testuser', password='testpassword')

        response = self.client.get(reverse('edit_news', kwargs={'news_id': news.id}))
        # Ожидаем редирект на страницу входа, используя правильный URL
        self.assertRedirects(response, '/login/?next=' + reverse('edit_news', kwargs={'news_id': news.id}))
