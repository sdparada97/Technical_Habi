# Core Library
import os
from pathlib import Path

# Third party
from dotenv import load_dotenv
from werkzeug.exceptions import HTTPException, Unauthorized
from werkzeug.routing import Map, Rule, Submount
from werkzeug.wrappers import Request, Response

# First party
from app.views.property import get_properties

dotenv_path = Path(__file__).parent.parent / ".env.local"
load_dotenv(dotenv_path)

API_KEY = os.getenv('API_KEY')


def check_auth(request):
    api_key = request.headers.get('X-API-Key')
    if api_key != API_KEY:
        raise Unauthorized('API Key inválida')


class App(object):
    def __init__(self):
        self.url_map = Map([
            Rule('/', endpoint=home),
            Submount('/properties', [
                Rule('/', methods=['GET'], endpoint=self.authenticated(get_properties)),
            ])
        ])

    def authenticated(self, f):
        def wrapper(request, *args, **kwargs):
            check_auth(request)
            return f(request, *args, **kwargs)
        return wrapper

    def dispatch_request(self, request):
        map_adapter = self.url_map.bind_to_environ(request.environ)
        try:
            endpoint, values = map_adapter.match()
            return endpoint(request, **values)
        except HTTPException as e:
            return e

    def wsgi_app(self, environ, start_response):
        request = Request(environ)
        response = self.dispatch_request(request)
        return response(environ, start_response)

    def __call__(self, environ, start_response):
        return self.wsgi_app(environ, start_response)


def home(request: Request):
    return Response('Hello, World')
