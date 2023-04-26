from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model
from django.db.models import Q

class EmailOrUsernameModelBackend(BaseBackend):
    """
    Authentication backend that allows a user to log in using their email
    address or username.
    """
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()

        if username is None or password is None:
            return None

        try:
            # Try to fetch the user by their email address
            user = UserModel.objects.filter(Q(email=username)|Q(username=username)).first()
        except UserModel.DoesNotExist:
                return None

        # Check if the password is correct
        return user if user and user.check_password(password) else None