from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


class BaseHandler(View):
    _status_code = 200

    def dispatch(self, request, *args, **kwargs):
        # self._request = request
        if request.method.lower() in self.http_method_names:
            handler = getattr(self, request.method.lower(),
                              self.http_method_not_allowed)
        else:
            handler = self.http_method_not_allowed
        return handler(*args, **kwargs)

    @property
    def remote_ip(self):
        return self.request.META.get('REMOTE_ADDR', 'unknown')

    @property
    def user_agent(self):
        return self.request.META.get('HTTP_USER_AGENT', 'unknown')

    def render_to_response(self, view_url, kwargs):
        return render(self.request, view_url, kwargs)

    def _response(self, *args, **kwargs):
        return HttpResponse(status=self._status_code,
                            *args, **kwargs)

    def response_ok(self, *args, **kwargs):
        return self._response(*args, **kwargs)

    def response_fail(self, *args, **kwargs):
        status = 400
        return self._response(status=status, *args, **kwargs)

    def redirect(self):
        pass
