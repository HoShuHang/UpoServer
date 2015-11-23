from django.test import TestCase
from core.account.user_manager import UserManager
from core.utility.utility import Utility


class TestUserManager(TestCase):
    def setUp(self):
        self._user_manager = UserManager()

    def test_register(self):
        fb_token = Utility.generate_token()
        user = self._user_manager.register(fb_token)
        self.assertEqual(fb_token, user.fb_token, "fb token error")

    def tearDown(self):
        pass