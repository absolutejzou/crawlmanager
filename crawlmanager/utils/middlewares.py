import json

from django.contrib.auth import REDIRECT_FIELD_NAME
from django.http import HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin

from crawlmanager.res import messages
from crawlmanager.utils.handlers import response as response_handler
from crawlmanager.utils.status import is_client_error, is_server_error


# 解决ajax无法重定向的问题
class AjaxRedirect(MiddlewareMixin):
    def process_response(self, request, response):
        if request.is_ajax():
            if type(response) == HttpResponseRedirect:
                response.status_code = 278
        return response


# 服务器各种异常统一处理
class ErrorHandler(MiddlewareMixin):
    def process_response(self, request, response):
        status_code = response.status_code
        if is_client_error(status_code) or is_server_error(status_code):
            if (request.method == 'GET' and
                        type(response) != HttpResponseRedirect):
                return HttpResponseRedirect(request.GET.get(REDIRECT_FIELD_NAME,
                                                            '/'))
            elif request.method == 'POST':
                if 'result' not in json.loads(response.content):
                    message = messages.HTTP_ERROR.get(
                        status_code, messages.HTTP_UNKNOWN_ERROR)
                    return response_handler(message=message, status=status_code)
            else:
                return response
        return response
