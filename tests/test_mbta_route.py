#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for obtaining Route objects from MBTA object"""

import unittest
from unittest import mock
from mbta.mbta import MBTA
from mbta.query_engine.engine import Engine

DATA = {
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
    'relationships': {
        'line': {
            'data': {
                'id': 'line-747',
                'type': 'line'
            }
        }
    }
}

MULTI_VAL = [DATA] * 10


class Test_MBTA_Route(unittest.TestCase):
    """Tests for obtaining Route objects from MBTA Object"""

    def setUp(self):
        self.mbta = MBTA('secret_key')

    def test_get_route(self):
        with mock.patch.object(Engine, 'request', return_value=DATA):
            route = self.mbta.route(747)
            # Attribute Tests
            self.assertEqual(route.color, DATA['attributes']['color'])
            self.assertEqual(route.description, DATA['attributes']['description'])
            self.assertEqual([*route.destinations], DATA['attributes']['direction_destinations'])
            self.assertEqual([*route.directions], DATA['attributes']['direction_names'])
            self.assertEqual(route.fare_class, DATA['attributes']['fare_class'])
            self.assertEqual(route.long_name, DATA['attributes']['long_name'])
            self.assertEqual(route.text_color, DATA['attributes']['text_color'])

            # Relationship Tests
            self.assertEqual(route.line, DATA['relationships']['line']['data']['id'])

    def test_get_routes(self):
        with mock.patch.object(Engine, 'request', return_value=MULTI_VAL):
            routes = self.mbta.routes()
            routes.count(routes[0]) == len(routes)
