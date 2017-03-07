from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from crawlmanager.utils.handler import BaseView


class Home(BaseView):
    def get(self):
        return self.render_to_response('foundation/index.html',
                                       {'title': 'haha'})

    def post(self):
        return self.response({})


class Test(BaseView):
    def get(self, id):
        return self.response({'id': id})


class Signup(BaseView):
    def post(self, request):
        u = User.objects.create_user(
            username='jzou',
            email='12345@td.com',
            password='1234'
        )
        u.save()
        return self.response({"ok": True})


class Login(BaseView):
    def get(self, request):
        return self.render_to_response('foundation/login.html', {})

    def post(self, request):
        user = authenticate(username='jzou', password='1234')
        login(request, user)
        return self.response({'ok': True})


class Logout(BaseView):
    def get(self, request):
        logout(request)
        return self.response({'ok': True})
