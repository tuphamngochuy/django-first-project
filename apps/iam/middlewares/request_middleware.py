from django.http import HttpRequest, HttpResponse
import logging
from rest_framework.response import Response

class RequestMiddleware:
    logger = logging.getLogger("iam_logger")
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: HttpRequest) -> HttpResponse:
        if request.path.startswith('/api/iam/'):
            try:
                self.logger.debug(f'Request: {request.method} {request.path}')
                response = self.get_response(request)
                self.logger.info(f'Response: {response.status_code}')
                return response
            except Exception as e:
                self.logger.error(f'Error: {e}')
                return Response(str(e), status=500)
        return self.get_response(request)