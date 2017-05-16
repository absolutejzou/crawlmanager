from django.http import JsonResponse


# class BaseView(APIView):
#
#     @property
#     def remote_ip(self):
#         return self.request.META.get('REMOTE_ADDR', 'unknown')
#
#     @property
#     def user_agent(self):
#         return self.request.META.get('HTTP_USER_AGENT', 'unknown')
#
#     def render_to_response(self, template_name, context):
#         return render(self.request, template_name, context=context)
#
#     def response(self, message, status=None):
#         data = {
#             'ok': True if not status or is_success(status) else False,
#             'result': message
#         }
#         return Response(data, status=status)
from crawlmanager.utils.status import is_success


def response(message, status=None):
        data = {
            'ok': True if not status or is_success(status) else False,
            'result': message
        }
        return JsonResponse(data, status=status)
