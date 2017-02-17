from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template

from rest_framework.views import View


class Home(View):
    def get(self, request):
        t = get_template("foundation/index.html")
        return HttpResponse(t.render(Context({'title': 'test'})))

    def post(self, request):
        return HttpResponse('hello world!')
