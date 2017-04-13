from django.core.urlresolvers import reverse
from django.test import TestCase


class TestIndexView(TestCase):
    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/cv/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('cv:index'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('cv:index'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'cv/index.html')


class TestEducationView(TestCase):
    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/cv/education/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('cv:education'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('cv:education'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'cv/education.html')


class TestExperienceView(TestCase):
    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/cv/experience/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('cv:experience'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('cv:experience'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'cv/experience.html')


class TestSkillsView(TestCase):
    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/cv/skills/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('cv:skills'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('cv:skills'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'cv/skills.html')


class TestMembershipsView(TestCase):
    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/cv/memberships/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('cv:memberships'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('cv:memberships'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'cv/memberships.html')


class TestProjectsView(TestCase):
    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/cv/projects/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('cv:projects'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('cv:projects'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'cv/projects.html')


class TestPublicationsView(TestCase):
    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/cv/publications/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('cv:publications'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('cv:publications'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'cv/publications.html')


class TestHtmlView(TestCase):
    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/cv/html/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('cv:html'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('cv:html'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'cv/html.html')


class TestPdfView(TestCase):
    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/cv/pdf/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('cv:pdf'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('cv:pdf'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'cv/pdf.html')
