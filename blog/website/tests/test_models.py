from django.test import TestCase
from django.contrib.auth.models import User
from ..models import Article, Comment

class ArticleModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.article = Article.objects.create(
            title="Test Article",
            content="This is a test article content.",
            author=self.user
        )

    def test_article_model(self):
        article = Article.objects.get(id=self.article.id)
        self.assertEqual(article.title, "Test Article")
        self.assertEqual(article.content, "This is a test article content.")
        self.assertEqual(article.author, self.user)

class CommentModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.article = Article.objects.create(
            title="Test Article",
            content="This is a test article content.",
            author=self.user
        )
        self.comment = Comment.objects.create(
            article=self.article,
            author=self.user,
            text="This is a test comment."
        )

    def test_comment_model(self):
        comment = Comment.objects.get(id=self.comment.id)
        self.assertEqual(comment.article, self.article)
        self.assertEqual(comment.author, self.user)
        self.assertEqual(comment.text, "This is a test comment.")
