from django.db import IntegrityError
from core.account.user import User
from core.utility.error_exceptions import FbTokenExistedError
from core.utility.utility import Utility


class UserManager():
    def __init__(self):
        pass

    def register(self, fb_token):
        uid = Utility.hash_to_key(fb_token)
        token = Utility.generate_token()

        try:
            user = User.objects.create(user_id=uid, access_token=token, fb_token=fb_token)
        except IntegrityError:
            raise FbTokenExistedError()
        return user
