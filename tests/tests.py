# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest

import django
from django.test import TestCase

from requests import codes

import local_requests
from local_requests import utils


class UtilsTest(unittest.TestCase):
    def test_convert_headers_to_environ(self):
        headers = {
            'Content-Type': 'application/json',
        }
        self.assertEqual(utils.convert_headers_to_environ(headers), {
            'HTTP_CONTENT_TYPE': 'application/json',
        })


class BasicSessionAPITest(TestCase):
    def test_get_api_root(self):
        url = 'http://testserver/api/'
        response = local_requests.get(url)
        self.assertEqual(response.status_code, codes.ok)
        self.assertEqual(response.json(), {
            'authors': 'http://testserver/api/authors/',
            'books': 'http://testserver/api/books/',
        })

    def test_post_data(self):
        url = 'http://testserver/api/authors/'
        response = local_requests.post(url, data={
            'name': 'J.K. Rowling',
        })
        self.assertEqual(response.status_code, codes.created)
        data = response.json()
        self.assertEqual(data['name'], 'J.K. Rowling')

    def test_post_data_using_json(self):
        url = 'http://testserver/api/authors/'
        response = local_requests.post(url, json={
            'name': 'J.K. Rowling',
        })
        self.assertEqual(response.status_code, codes.created)
        data = response.json()
        self.assertEqual(data['name'], 'J.K. Rowling')

    def test_sends_params(self):
        url = 'http://testserver/echo/'
        response = local_requests.get(url, headers={
            'user-agent': 'Mozilla/5.0',
        })
        self.assertEqual(response.status_code, codes.ok)
        data = response.json()
        self.assertEqual(data['META']['HTTP_USER_AGENT'], 'Mozilla/5.0')

    def test_sends_custom_headers(self):
        url = 'http://testserver/echo/'
        response = local_requests.get(url, params={
            'q': 'search',
        })
        self.assertEqual(response.status_code, codes.ok)
        data = response.json()
        self.assertEqual(data['GET']['q'], 'search')

    def test_sends_files(self):
        url = 'http://testserver/upload_file/'
        response = local_requests.post(url, files={
            'file': ('report.csv', 'ID,name\n1,Rocky'),
        })
        self.assertEqual(response.status_code, codes.ok)
        self.assertEqual(response.json(), {
            'name': 'report.csv',
            'content': 'ID,name\n1,Rocky',
        })

    def test_redirects(self):
        url = 'http://testserver/ehco/'
        response = local_requests.get(url, allow_redirects=False)
        self.assertEqual(response.status_code, codes.found)
        if django.VERSION < (1, 9):
            self.assertEqual(response.headers['Location'], 'http://testserver/echo/')
        else:
            self.assertEqual(response.headers['Location'], '/echo/')

        response = local_requests.get(url, allow_redirects=True)
        self.assertEqual(response.status_code, codes.ok)
        self.assertEqual(response.url, 'http://testserver/echo/')
        self.assertEqual(response.history[0].status_code, codes.found)
