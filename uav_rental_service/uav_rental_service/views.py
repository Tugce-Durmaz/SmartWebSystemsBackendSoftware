# views.py

from django.contrib.auth.views import LogoutView
from django.shortcuts import redirect

class CustomLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        redirect_url = '/accounts/login'  # veya başka bir URL
        return redirect(redirect_url)
