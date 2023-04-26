from django.db import models
from user.models import UserAccount, BaseModel
from notify.constants import (CATEGORIES, PLATFORM, TRIGGER, FREQUENCY, STATUS)


class UserNotification(BaseModel):
    """
    Store user defined notifications
    """
    user = models.ForeignKey(
        UserAccount, on_delete=models.CASCADE, related_name="user_notification"
    )
    category = models.CharField(max_length=30, choices=CATEGORIES)
    platform = models.CharField(max_length=30, choices=PLATFORM)
    trigger = models.CharField(max_length=30, choices=TRIGGER)
    frequency = models.CharField(max_length=30, choices=FREQUENCY) # how often the notification should be sent
    dateToBeSent = models.DateTimeField(auto_now_add=True)

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


class NotificationStatus(BaseModel):
    """
    record of how often notifications is sent
    """
    notification = models.ForeignKey(
        UserNotification, on_delete=models.CASCADE, related_name="user_notification"
    )
    status = models.CharField(max_length=30, choices=STATUS)
    