import time
from collections import defaultdict

class UserVisitLog():
    def __init__(self, get_response):
        self.get_response = get_response
        self.visits = defaultdict(int)
        self.last_login = dict()
        self.total_requests_served = 0
    
    def __call__(self, request):
        self.total_requests_served += 1
        response = self.get_response(request)
        if request.META.get('HTTP_REFERER') and '/login/' in request.META.get('HTTP_REFERER') and request.META['REQUEST_METHOD'] == 'POST' and response.status_code == 302:
            user = request.user
            self.visits[user] += 1
            secs = time.time()
            time_obj = time.gmtime(secs)
            time_str = time.asctime(time_obj)
            self.last_login[user] = time_str
        return response
    
    def process_view(self, request, view_func, *view_args, **view_kwargs):
        user = request.user
        if user in self.last_login:
            last_login = self.last_login[user]
        else:
            last_login = '--|--|--'
        request.last_login = last_login
        request.visits = self.visits[user]
        request.total_request = self.total_requests_served