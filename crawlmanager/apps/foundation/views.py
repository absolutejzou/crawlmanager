from django.http import HttpResponse
from django.shortcuts import render

from rest_framework.views import View


class Home(View):
    def get(self, request):
        return render(request, 'foundation/index.html', {'title': 'haha'})

    def post(self, request):
        return HttpResponse('hello world!')
