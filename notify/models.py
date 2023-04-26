from django.db import models
from user.models import UserAccount, BaseModel
from notify.constants import CATEGORIES, PLATFORM, TRIGGER

# Create your models here.
class UserNotification(BaseModel):
    user = models.ForeignKey(
        UserAccount, on_delete=models.CASCADE, related_name="user_notification"
    )
    category = models.CharField(max_length=30, choices=CATEGORIES)
    platform = models.CharField(max_length=30, choices=PLATFORM)
    trigger = models.CharField(max_length=30, choices=TRIGGER)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=[
                    "user",
                    "category",
                    "platform",
                    "trigger",
                ],
                name="unique_notification",
            )
        ]
