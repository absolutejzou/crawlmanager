from crawlmanager.apps.foundation.models import User
from crawlmanager.utils.handler import BaseHandler

from django.views import generic


class Home(BaseHandler):
    def get(self):
        return self.render_to_response('foundation/index.html',
                                       {'title': 'haha'})

    def post(self):
        return self.response({})


class Test(BaseHandler):
    def get(self, id):
        return self.response_ok({'id': id})
