# Create your tests here.
import sys

from django.test import TestCase

from blog.models import Category, Blog

# override the old unicode() function to just call str() on python 3
if sys.version_info.major == 3:
    unicode = str


class TestCategory(TestCase):
    def setUp(self):
        self.c = Category(title="My Title")

    def test_unicode(self):
        self.assertEqual(self.c.title, unicode(self.c))

    def test_str(self):
        self.assertEqual(self.c.title, str(self.c))


class TestBlog(TestCase):
    def setUp(self):
        self.b = Blog(title="My Title")

    def test_unicode(self):
        self.assertEqual(self.b.title, unicode(self.b))

    def test_str(self):
        self.assertEqual(self.b.title, str(self.b))
