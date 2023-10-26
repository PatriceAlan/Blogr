from django.test import TestCase
from django.contrib.auth.models import User
from ..forms import SignUpForm, AddArticleForm, CommentForm

class SignUpFormTest(TestCase):
    def test_valid_signup_form(self):
        form = SignUpForm(data={
            'username': 'testuser',
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'test@example.com',
            'password1': 'testpassword',
            'password2': 'testpassword',
        })
        self.assertTrue(form.is_valid())

    def test_invalid_signup_form(self):
        form = SignUpForm(data={})  # No data provided
        self.assertFalse(form.is_valid())

class AddArticleFormTest(TestCase):
    def test_valid_add_article_form(self):
        form = AddArticleForm(data={
            'title': 'Test Article',
            'content': 'This is a test article content',
        })
        self.assertTrue(form.is_valid())

    def test_invalid_add_article_form(self):
        form = AddArticleForm(data={})  # No data provided
        self.assertFalse(form.is_valid())

class CommentFormTest(TestCase):
    def test_valid_comment_form(self):
        form = CommentForm(data={'text': 'This is a test comment.'})
        self.assertTrue(form.is_valid())

    def test_invalid_comment_form(self):
        form = CommentForm(data={})  # No data provided
        self.assertFalse(form.is_valid())
