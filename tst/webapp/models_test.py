from django.test import TestCase
from webapp.models import Profile
from webapp.models import User

class ModelsTest(TestCase):
    def test_profile(self):
        user = User.objects.create(email='test@gmail.com', password='password', first_name='John', last_name='Doe')
        profile = Profile.objects.create(user_id=1, phone_number='123-4567', role=Profile.Roles.CUSTOMER)

        self.assertTrue(user, isinstance(User))
        self.assertTrue(profile, isinstance(Profile))



