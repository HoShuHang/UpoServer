from django.db import models

class UserModel(models.Model):
    user_id = models.BigIntegerField(unique=True, blank=False, null=False, primary_key=True)
    access_token = models.CharField(max_length=50, blank=False, null=False, unique=True)

    fb_token = models.CharField(max_length=50, blank=False, null=False, unique=True)

    notification_token = models.CharField(max_length=180, default='')

    class Meta:
        db_table = "user"