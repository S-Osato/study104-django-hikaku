from django.contrib.auth.views import (
    LoginView, LogoutView
)

class Logout(LogoutView):
    """ログアウトページ"""
    template_name = 'hikaku/logout.html'