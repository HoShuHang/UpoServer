import json
from rest_framework.test import APITestCase
from core.account.user import User


class RegisterAPITestCase(APITestCase):
    def setUp(self):
        pass

    def test_register(self):
        # self.assertTrue("account" in data)
        # self.client.credentials(HTTP_AUTHORIZATION="ewfjkknw")
        response = self.client.post("/api/user/register", {
            "fb_token": "abcde"
        })
        json_data = json.loads(response.content.decode("utf-8"))
        user = User.objects.get(fb_token="abcde")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json_data["access_token1"], user.token)

    def tearDown(self):
        pass
