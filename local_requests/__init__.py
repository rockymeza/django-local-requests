# -*- coding: utf-8 -*-
"""
A client for your local Django project that emulates the requests API.
"""
import pkg_resources
from io import BytesIO

from django.test import Client as TestClient

import requests
from requests.adapters import HTTPAdapter

from .utils import convert_headers_to_environ

__version__ = pkg_resources.get_distribution('django-local-requests').version
__author__ = 'Rocky Meza'
__email__ = 'rockymeza@gmail.com'


class FakeHttpResponse(object):
    """
    This class proxies enough of the interface of urllib3.response.HttpResponse
    through to a django.http.HttpResponse to fool requests.
    """
    def __init__(self, django_response):
        self._response = django_response

        self.status = django_response.status_code
        self.reason = django_response.reason_phrase
        self.headers = dict(django_response.items())
        self.read = BytesIO(self._response.content).read

    def release_conn(self, *args, **kwargs):
        """
        Don't actually need to release the connection back to the pool because
        there never was a connection.
        """


class MyTestClient(TestClient):
    def _base_environ(self, *args, **kwargs):
        environ = super(MyTestClient, self)._base_environ(*args, **kwargs)
        # XXX: The FakePayload object that the Test client uses is not JSON
        # serializable.
        environ['wsgi.input'] = BytesIO(environ['wsgi.input'].read())
        return environ


class LocalDjangoAdaptor(HTTPAdapter):
    """
    A Transport Adaptor for requests that just calls into Django using the
    TestClient.
    """
    def __init__(self):
        self.client = MyTestClient()

    def send(self, request, *args, **kwargs):
        url = self.request_url(request, kwargs.get('proxies'))
        self.add_headers(request)

        method = request.method.lower()
        handler = getattr(self.client, method)
        django_response = handler(
            path=url,
            data=request.body,
            content_type=request.headers.get('Content-Type'),
            secure=request.url.startswith('https://'),
            **convert_headers_to_environ(request.headers)
        )

        return self.build_response(request, FakeHttpResponse(django_response))

    def close(self, *args, **kwargs):
        """
        This is part of the required interface, but not required for our
        adapter.
        """


class Session(requests.Session):
    def __init__(self, *args, **kwargs):
        super(Session, self).__init__(*args, **kwargs)
        self.mount('http://', LocalDjangoAdaptor())
        self.mount('https://', LocalDjangoAdaptor())


def request(method, url, **kwargs):
    with Session() as session:
        return session.request(method=method, url=url, **kwargs)


def _request_method(method_name):
    def method(*args, **kwargs):
        return request(method_name, *args, **kwargs)
    method.__name__ = method_name.lower()
    return method


get = _request_method('GET')
options = _request_method('OPTIONS')
head = _request_method('HEAD')
post = _request_method('POST')
put = _request_method('PUT')
patch = _request_method('PATCH')
delete = _request_method('DELETE')
