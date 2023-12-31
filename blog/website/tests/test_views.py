from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from ..models import Article
from django.test import Client

class ViewsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.client = Client()

    def test_home_view(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "user/home.html")

    def test_add_article_view(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("add_article"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "article/add_article.html")

    def test_article_detail_view(self):
        article = Article.objects.create(
            title="Test Article",
            content="This is a test article content.",
            author=self.user
        )
        response = self.client.get(reverse("article_detail", args=[article.pk]))
        self.assertEqual(response.status_code, 302)

    def test_user_detail_view(self):
        response = self.client.get(reverse("user_detail", args=[self.user.pk]))
        self.assertEqual(response.status_code, 302)


    def test_register_user_view(self):
        response = self.client.get(reverse("register"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "user/register.html")

    def test_logout_user_view(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("logout"))
        self.assertEqual(response.status_code, 302)

