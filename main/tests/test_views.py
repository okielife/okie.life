from django.core.urlresolvers import reverse
from django.test import TestCase


class TestIndexView(TestCase):

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('root-index'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('root-index'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'index.html')


class TestHumansView(TestCase):

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/humans.txt')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('humans'))
        self.assertEqual(resp.status_code, 200)
