#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `Route` class"""

import unittest
from mbta.route.route import Route

ref_attr = {
    "color": "DA291C",
    "description": "Rapid Transit",
    "direction_destinations": [
        "Ashmont/Braintree",
        "Alewife"
    ],
    "direction_names": [
        "South",
        "North"
    ],
    "fare_class": "Rapid Transit",
    "long_name": "Red Line",
    "short_name": "",
    "sort_order": 10010,
    "text_color": "FFFFFF",
    "type": 1
}

ref_rel = {
    "line": {
        "data": {
            "id": "line-Red",
            "type": "line"
        }
    }
}

class TestRoute(unittest.TestCase):
    """Unit tests for `Route` class"""

    def setUp(self):
        self.route = Route('red', ref_attr, ref_rel)

    def test_id(self):
        self.assertEqual(self.route.id, 'red')

    def test_color(self):
        self.assertEqual(self.route.color, ref_attr['color'])

    def test_text_color(self):
        self.assertEqual(self.route.text_color, ref_attr['text_color'])

    def test_description(self):
        self.assertEqual(self.route.description, ref_attr['description'])

    def test_destinations(self):
        dest_0, dest_1 = self.route.destinations
        self.assertEqual(dest_0, ref_attr['direction_destinations'][0])
        self.assertEqual(dest_1, ref_attr['direction_destinations'][1])

    def test_directions(self):
        d_0, d_1 = self.route.directions
        self.assertEqual(d_0, ref_attr['direction_names'][0])
        self.assertEqual(d_1, ref_attr['direction_names'][1])

    def test_fare_class(self):
        self.assertEqual(self.route.fare_class, ref_attr['fare_class'])

    def test_long_name(self):
        self.assertEqual(self.route.long_name, ref_attr['long_name'])

    def test_short_name(self):
        self.assertEqual(self.route.short_name, ref_attr['short_name'])

    def test_route_type(self):
        self.assertEqual(self.route.route_type, ref_attr['type'])

    def test_line(self):
        self.assertEqual(self.route.line, ref_rel['line']['data']['id'])
