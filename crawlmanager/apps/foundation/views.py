
from crawlmanager.utils.handler import BaseHandler


class Home(BaseHandler):
    def get(self):
        return self.render_to_response('foundation/index.html',
                                       {'title': 'haha'})

    def post(self):
        return self.response_ok()


class Test(BaseHandler):
    def get(self, id):
        print(id)
        return self.response_ok({'id': id})
