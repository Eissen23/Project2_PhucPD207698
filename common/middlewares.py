from django.utils.deprecation import MiddlewareMixin

from common.threadlocals import set_current_user, clear_current_user


class CurrentUserMiddleware(MiddlewareMixin):
    def process_request(self, request):
        set_current_user(
            request.user if request.user.is_authenticated else None,
        )
    def process_response(self, request, response):
        clear_current_user()
        return response

    def process_exception(self, request, exception):
        clear_current_user()