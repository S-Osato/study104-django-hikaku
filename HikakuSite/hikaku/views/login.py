from django.contrib.auth.views import (
    LoginView, LogoutView
)
from ..forms import LoginForm

class Login(LoginView):
    """ログインページ"""
    form_class = LoginForm
    template_name = 'hikaku/login.html'