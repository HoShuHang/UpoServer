from core.models import UserModel


class User(UserModel):
    class Meta:
        proxy = True

    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)

    @property
    def token(self):
        return self.access_token
