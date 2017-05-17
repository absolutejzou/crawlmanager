from django.http import JsonResponse

from crawlmanager.utils.status import is_success


def response(message, status=None):
        data = {
            'ok': True if not status or is_success(status) else False,
            'result': message
        }
        return JsonResponse(data, status=status)
