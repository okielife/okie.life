from django.core.urlresolvers import reverse
from django.test import TestCase


class TestIndexView(TestCase):

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/family/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('family:index'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('family:index'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'family/index.html')
