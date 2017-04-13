from django.core.urlresolvers import reverse
from django.test import TestCase


class TestIndexView(TestCase):

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/consulting/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('consulting:index'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('consulting:index'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'consulting/index.html')


class TestStatusView(TestCase):

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/consulting/status/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('consulting:status'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('consulting:status'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'consulting/status.html')
