import re
from django.conf import settings
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth import logout

LOGIN_FREE_URLS = []
EXEMPT_URLS = []

LOGIN_FREE_URLS += [re.compile(url) for url in settings.LOGIN_FREE_URLS]
EXEMPT_URLS += [re.compile(url) for url in settings.EXEMPT_URLS]

class LoginRequiredMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        assert hasattr(request, 'user')
        path = request.path_info.lstrip('/')
        url_is_exempt = any(url.match(path) for url in EXEMPT_URLS)
        url_is_free = any(url.match(path) for url in LOGIN_FREE_URLS)

        if path == reverse('organisations:logout').lstrip('/'):
            logout(request)

        if (not request.user.is_authenticated() and url_is_exempt):

            return redirect(settings.HOME_REDIRECT_URL)
        elif request.user.is_authenticated() and url_is_free:
            return redirect(settings.HOME_REDIRECT_URL)
        else:
            return None
