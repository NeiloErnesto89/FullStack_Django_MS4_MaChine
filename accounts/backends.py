from django.contrib.auth.models import User


class EmailAuth:
    """
    Authenticate User - Simple class with methods so user can sign 
    in with email address instead of username
    """

    def authenticate(self, username=None, password=None):  # **kwargs

        # get instance of user using details #

        try:
            user = User.objects.get(email=username)

            if user.check_password(password):
                return user

            return None

        except User.DoesNotExist:
            return None

    def get_user(self, user_id):

        # method retrieves user instances via Django auth sys
            
        try:
            user = User.objects.get(pk=user_id)

            if user.is_active:
                return user

            return None
        except User.DoesNotExist:
            return None
