from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.models import User
from django.forms import EmailField


class CustomUserCreationForm(UserCreationForm):
    
    email = EmailField(
        required=True,
        help_text="Enter a valid Email, like : example@email.com")

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email',)
        field_classes = {
            "username": UsernameField,
            "email": EmailField,
        }
