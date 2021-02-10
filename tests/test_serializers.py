from django.test import TestCase

from tinder.models import User

from API.serializers import UserSerializer


class UserSerializerTest(TestCase):
    def setUp(self):
        self.user_attributes = {
            "first_name": "Alex",
            "last_name": "Zubritskiy",
            "email": "Zubritskiy@gmail.com",
            "sex": "1",
            "age": "20",
            "description": "sdfghjkhvnabdsmnv",
            "subscription": "VIP"
        }

        self.serializer_data = {
            "first_name": "Alina",
            "last_name": "Petuh",
            "email": "Petuh@gmail.com",
            "sex": "2",
            "age": "23",
            "description": "asavbj,zhsbdjhgali",
            "subscription": "premium"
        }

        self.staff = User.objects.create(**self.user_attributes)
        self.serializer = UserSerializer(instance=self.staff, context={'request': None})

    def test_first_name_field_content(self):
        data = self.serializer.data
        self.assertEqual(data["first_name"], self.user_attributes["first_name"])

    def test_last_name_field_content(self):
        data = self.serializer.data
        self.assertEqual(data["last_name"], self.user_attributes["last_name"])

    def test_email_field_content(self):
        data = self.serializer.data
        self.assertEqual(data["email"], self.user_attributes["email"])

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), {"first_name", "last_name", "phone_number", "id", "sex", "url", "email", "age","description", "subscription"})

    def test_sex_field_content(self):
        data = self.serializer.data
        self.assertEqual(data["sex"], self.user_attributes["sex"])

    def test_team_field_content(self):
        data = self.serializer.data
        self.assertEqual(data["age"], self.user_attributes["age"])

    def test_description_field_content(self):
        data = self.serializer.data
        self.assertEqual(data["description"], self.user_attributes["description"])

    def test_subscription_field_content(self):
        data = self.serializer.data
        self.assertEqual(data["subscription"], self.user_attributes["subscription"])
