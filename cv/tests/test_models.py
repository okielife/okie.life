from django.test import TestCase

from cv.models import Person


class PersonModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # this method is called once per class, so it should only instantiate static things
        Person.objects.create(
            name="Person Jones",
            email="person.jones@somehow.com",
            github_id="personj",
            goal="My goal is to blah blah."
        )

    def test_name_max_length_ok(self):
        person = Person.objects.get(id=1)
        max_len = person._meta.get_field('name').max_length
        self.assertEqual("Person Jones", person.name)
        self.assertEqual(max_len, 100)

        # def test_get_absolute_url(self):
        #     person = Person.objects.get(id=1)
        #     # This will also fail if the urlconf is not defined.
        #     self.assertEquals(person.get_absolute_url(),'/cv/person/1')
