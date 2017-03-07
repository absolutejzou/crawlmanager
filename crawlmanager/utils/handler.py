import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from rest_framework.views import APIView


def utf8(value):
    if isinstance(value, (bytes, type(None))):
        return value
    return value.encode('utf-8')


class BaseView(APIView):
    _status_code = 200
    @property
    def remote_ip(self):
        return self.request.META.get('REMOTE_ADDR', 'unknown')

    @property
    def user_agent(self):
        return self.request.META.get('HTTP_USER_AGENT', 'unknown')

    def render_to_response(self, view_url, kwargs):
        return render(self.request, view_url, kwargs)

    def _response(self, chunk=None):
        return HttpResponse(status=self._status_code, content=chunk)

    def response(self, chunk):
        if isinstance(chunk, dict):
            chunk = json.dumps(chunk).replace("</", "<\\/")
        chunk = utf8(chunk)
        return self._response(chunk)

    def response_error(self, *args, **kwargs):
        self._status_code = 400
        return self._response(*args, **kwargs)

    def redirect(self):
        pass
