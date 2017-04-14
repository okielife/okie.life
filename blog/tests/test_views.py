from django.core.urlresolvers import reverse
from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Category, Blog


class TestIndexView(TestCase):

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/blog/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('blog:index'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('blog:index'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'blog/index.html')


class TestBlogView(TestCase):

    def setUp(self):
        self.c = Category(title="MyTitle")
        self.c.save()
        self.b = Blog(title="BlogTitle", category=self.c)
        self.b.save()

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/blog/posts/%s/' % self.b.id)
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('blog:view_blog_post', args=(self.b.id,)))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('blog:view_blog_post', args=(self.b.id,)))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'blog/view_post.html')


class TestBlogCreateAnonymousView(TestCase):

    def test_redirects_to_login_page(self):
        response = self.client.get(reverse('blog:create_blog'))
        self.assertRedirects(response, '/accounts/login/?next=/blog/posts/')
        # TODO: Need to assert that it redirects to the right page on ?next


class TestBlogCreateLoggedInView(TestCase):

    def setUp(self):
        User.objects.create_user(username='username', password='password')
        self.client.login(username='username', password='password')

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/blog/posts/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('blog:create_blog'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('blog:create_blog'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'blog/blog_form.html')

    def test_post_works(self):
        # first get the initial response
        r = self.client.get(reverse('blog:create_blog'))
        # then get the form instance from that, it is unbound, but should contain the keys
        f = r.context['form']
        # if we ever wanted to test that the form was pre-populated, just check f.initial here
        data = dict(f.fields)
        data['title'] = 'TitleName'
        data['body'] = 'BodyOfPost'
        c = Category.objects.create(title='NewCategory')
        data['category'] = c.id
        resp = self.client.post(reverse('blog:create_blog'), data)
        posts_after = Blog.objects.all()
        self.assertEqual(resp.status_code, 302)
        self.assertRedirects(resp, reverse('blog:view_blog_post', args=(1,)))


class TestCategoryView(TestCase):

    def setUp(self):
        self.c = Category(title="MyTitle")
        self.c.save()

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/blog/categories/%s/' % self.c.id)
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('blog:view_blog_category', args=(self.c.id,)))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('blog:view_blog_category', args=(self.c.id,)))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'blog/view_category.html')


class TestCategoriesView(TestCase):

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/blog/categories/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('blog:view_blog_categories'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('blog:view_blog_categories'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'blog/view_categories.html')
