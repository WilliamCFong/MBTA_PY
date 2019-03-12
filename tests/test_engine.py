#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `engine` object."""

import unittest
import json
from unittest.mock import patch
from mbta.query_engine.engine import Engine
from mbta.exceptions import *

class MockRequest:
    def __init__(self, json_data, status_code):
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
         return self.json_data

def mock_error(*args, **kwargs):
    return MockRequest(json.loads(
            '{"errors":[{"title": "NotFound", "status": "404", "source": {"parameter": "id"}, "code": "not_found"}]}'
        ),
        404
    )

DATA = {
    'data': {
        'attributes': {
            'color': 'FFC72C',
            'description': 'Local Bus',
            'direction_destinations': [
                'Sullivan',
                'Ruggles'
            ],
            'direction_names': [
                'Outbound',
                'Inbound'
            ],
            'fare_class': 'Local Bus',
            'long_name': 'Sullivan - Ruggles',
            'short_name': 'CT2',
            'sort_order': 40020,
            'text_color': '000000',
            'type': 3
        },
        'id': '747',
        'links': {
            'self': '/routes/747'
        },
        'relationships': {
            'line': {
                'data': {
                    'id': 'line-747',
                    'type': 'line'
                }
            }
        },
        'type': 'route'
    },
    'jsonapi': {
        'version': '1.0'
    }
}

class TestEngine(unittest.TestCase):
    """Tests for `engine` object."""

    def setUp(self):
        self.engine = Engine('APIKEY')

    def test_apikey_persistence(self):
        self.assertEqual(self.engine.api_key, 'APIKEY')

    def test_no_api_set(self):
        with self.assertRaises(ValueError):
            self.engine.api_key = 'ILLEGAL'

    def test_set_user_agent(self):
        self.engine.user_agent = 'NEW UA'
        self.assertEqual(self.engine.user_agent, 'NEW UA')

    @patch('requests.get', side_effect=lambda *a, **kw: MockRequest(DATA, 200))
    def test_clean_request(self, mock):
        r = self.engine.request('base_route')
        filtered_data = {key: DATA['data'][key] for key in {'id', 'attributes', 'relationships'}}
        self.assertEqual(r, filtered_data)

    @patch('requests.get', side_effect=mock_error)
    def test_handle_404(self, mock):
        with self.assertRaises(MBTA_NotFound):
            self.engine.request('bad_route')

    @patch('requests.get', side_effect=lambda *a, **kw: MockRequest(DATA, 403))
    def test_handle_403(self, mock):
        with self.assertRaises(MBTA_Forbidden):
            self.engine.request('bad_route')

    @patch('requests.get', side_effect=lambda *a, **kw: MockRequest(DATA, 429))
    def test_handle_quota_exceeded(self, mock):
        with self.assertRaises(MBTA_QuotaExceeded):
            self.engine.request('too_many')
