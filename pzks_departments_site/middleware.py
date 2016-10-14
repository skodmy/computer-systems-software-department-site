
from django.conf import settings
from django.shortcuts import redirect


class LocaleMiddleware(object):

    def process_request(self, request):
        if request.path == '/':
            return redirect('/%s/' % settings.LANGUAGE_CODE)
