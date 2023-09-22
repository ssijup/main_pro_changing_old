import threading


_thread_locals = threading.local()

class CurrentUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print("User at start of custom middleware:", request.user)
        _thread_locals.user = request.user
        response = self.get_response(request)
        print("User at end of custom middleware:", request.user)

        return response
    

def get_current_user():
    return getattr(_thread_locals, 'user', None)

