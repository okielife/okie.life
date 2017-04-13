# Create your tests here.
import sys

from django.test import TestCase

from blog.models import Category, Blog


class TestCategory(TestCase):
    def setUp(self):
        self.c = Category(title="My Title")

    def test_string_reprs(self):
        # always check str
        self.assertEqual(self.c.title, str(self.c))
        # if we are on 2 then also check unicode
        if sys.version_info.major == 2:
            self.assertEqual(self.c.title, unicode(self.c))  # noqa: F821


class TestBlog(TestCase):
    def setUp(self):
        self.b = Blog(title="My Title")

    def test_string_reprs(self):
        # always check str
        self.assertEqual(self.b.title, str(self.b))
        # if we are on 2 then also check unicode
        if sys.version_info.major == 2:
            self.assertEqual(self.b.title, unicode(self.b))  # noqa: F821
