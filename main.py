from typing import Any
from response import Response


class MiniAPI:
    def __init__(self) -> None:
        self.routes = dict()

    def __call__(self, environ, start_response) -> Any:
        response = Response()
        for path, handler_dict in self.routes.items():
            for request_method, handler in handler_dict.items():
                if environ['REQUEST_METHOD'] == request_method and environ['PATH_INFO'] == path:
                    handler(environ, response)
                    response.as_wsgi(start_response)

                    return [response.text.encode()]
                
    def common_routes(self, path, handler, request_method):
        # {
            #     "/path": { 
            #         'GET': handler
            #     }
            # }
            path_name = path or f'/{handler.__name__}'
            if path_name not in self.routes:
                self.routes[path_name] = {}
            self.routes[path_name][request_method] = handler

            return request_method
    
    def get(self, path=None):
        def wrapper(handler):
            self.common_routes(path, handler, 'GET')

        return wrapper
    
    def post(self, path=None):
        def wrapper(handler):
            self.common_routes(path, handler, 'POST')

        return wrapper
    
    def delete(self, path=None):
        def wrapper(handler):
            self.common_routes(path, handler, 'DELETE')

        return wrapper
    
    def put(self, path=None):
        def wrapper(handler):
            self.common_routes(path, handler, 'PUT')

        return wrapper