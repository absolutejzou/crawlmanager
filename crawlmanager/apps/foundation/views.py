from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, REDIRECT_FIELD_NAME
from django.http import HttpResponseRedirect
from django.shortcuts import render

from crawlmanager.apps.foundation.validators import LoginForm
from crawlmanager.res import messages
from crawlmanager.utils import status
from crawlmanager.utils.handlers import response


@login_required
def home(request):
    return render(request, 'foundation/index.html', {'title': 'index'})


def page_not_found(request):
    return render(request, 'foundation/index.html', {'title': 'page not found'})


def sign_in(request):
    if request.method == 'GET':
        return render(request, 'foundation/login.html')
    else:
        form = LoginForm(request.POST)
        if not form.is_valid():
            return response(form.errors, status=status.HTTP_400_BAD_REQUEST)
        user = authenticate(username=form.cleaned_data['name'],
                            password=form.cleaned_data['password'])
        if not user:
            return response(messages.USER_OR_PASSWORD_ERROR,
                            status=status.HTTP_401_UNAUTHORIZED)
        if not user.is_active:
            return response(messages.USER_NOT_ACTIVE,
                            status=status.HTTP_401_UNAUTHORIZED)
        login(request, user)
        return HttpResponseRedirect(request.GET.get(REDIRECT_FIELD_NAME, '/'))


def sign_out(request):
    logout(request)
    return response({'ok': True})
