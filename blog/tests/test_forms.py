# from django.test import TestCase
# from blog.forms import BlogForm
# from blog.models import Blog


# class TestBlogCreateForm(TestCase):
#
#     def test_creation(self):
#         test_blog = Blog(title="This test blog")
#         test_blog_form = BlogForm(instance=test_blog)
#         self.assertEqual(test_blog_form.is_valid(), False)  # No data has been supplied yet.
#         test_blog_form = BlogForm({'title': "this title", }, instance=test_blog)
#         self.assertEqual(test_blog_form.is_valid(), True)  # Now that you have given it data, it can validate.
