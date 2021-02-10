from django.test import TestCase

from tinder.models import User


class UserModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create(first_name='Alex', last_name='Zubritskiy', email='Zubritskiy@gmail.com',

                            sex='1', age='20', subscription='premium', description='sadasdzbzx')

    def test_first_name_label(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('first_name').verbose_name
        self.assertEquals(field_label, 'First name')

    def test_last_name_label(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('last_name').verbose_name
        self.assertEquals(field_label, 'Last name')

    def test_phone_number_label(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('phone_number').verbose_name
        self.assertEquals(field_label, 'Phone number')

    def test_email_label(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('email').verbose_name
        self.assertEquals(field_label, 'Email')

    def test_age_label(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('age').verbose_name
        self.assertEquals(field_label, 'Age')

    def test_sex_label(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('sex').verbose_name
        self.assertEquals(field_label, 'Sex')

    def test_subscription_label(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('subscription').verbose_name
        self.assertEquals(field_label, 'Subscription')

    def test_description_label(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('description').verbose_name
        self.assertEquals(field_label, 'Description')


    def test_first_name_max_length(self):
        user = User.objects.get(id=1)
        max_length = user._meta.get_field('first_name').max_length
        self.assertEquals(max_length, 30)

    def test_last_name_label_max_length(self):
        user = User.objects.get(id=1)
        max_length = user._meta.get_field('last_name').max_length
        self.assertEquals(max_length, 30)

    def test_email_label_max_length(self):
        user = User.objects.get(id=1)
        max_length = user._meta.get_field('email').max_length
        self.assertEquals(max_length, 40)

    def test_description_max_length(self):
        user = User.objects.get(id=1)
        max_length = user._meta.get_field('description').max_length
        self.assertEquals(max_length, 255)

    def test_object_name(self):
        user = User.objects.get(id=1)
        expected_object_name = '%s, %s, %s, %s, %s' % (user.last_name, user.first_name, user.email, user.sex, user.description )
        self.assertEquals(expected_object_name, str(user))
