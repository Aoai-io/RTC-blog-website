from django.test import TestCase
from .models import Article
from django.contrib.auth.models import AnonymousUser, User


# Create your tests here.


class ModelTest(TestCase):
    def setUp(self):
        self.blog = Article.objects.create(
            title="article",
            cover=None,
            body="this is article body",
            author=User.objects.create(
                username="Osaka", email="osa#mail.com", password="12345678"
            ),
        )

    def test_article_title(self):
        d = self.blog
        self.assertEqual(str(d), "article")
