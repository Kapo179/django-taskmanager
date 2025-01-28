from django.contrib.auth.forms import UserCreationForm
from django.utils.html import format_html
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Field labels and IDs for accessibility
        self.fields['username'].widget.attrs.update({
            'id': 'id_signup_username',
            'aria-label': 'Username'
        })
        self.fields['password1'].widget.attrs.update({
            'id': 'id_signup_password1',
            'aria-label': 'Password'
        })
        self.fields['password2'].widget.attrs.update({
            'id': 'id_signup_password2',
            'aria-label': 'Password confirmation'
        })

        # Update help texts
        self.fields['password1'].help_text = format_html(
            """
            <ul>
                <li>Must be at least 8 characters long</li>
                <li>Cannot be entirely numeric</li>
                <li>Cannot be too similar to your personal information</li>
            </ul>
            """
        )
        self.fields['username'].help_text = "Letters, digits and @/./+/-/_ "
        self.fields['password2'].help_text = (
            "Enter the same password as before, for verification."
        ) 