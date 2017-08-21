from Products.Five.browser import BrowserView


class ManageStatusView(BrowserView):

    def __init__(self, context, request):
        BrowserView.__init__(self, context, request)
        self.response = request.response

    def __call__(self):
        return u''
