from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm



class SignupForm(UserCreationForm):
    pass



class SignInForm(AuthenticationForm):
    pass


class ChangePasswordForm(UserChangeForm):
    pass