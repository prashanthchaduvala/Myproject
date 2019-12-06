from django import forms
from .models import loginpage
class LoginForm(forms.ModelForm):
    class Meta:
        model=loginpage
        fields='__all__'
        widgets={'password':forms.PasswordInput}