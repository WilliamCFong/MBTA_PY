#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `Vehicle` class"""

import unittest
from dateutil.parser import parse
from mbta.vehicle.vehicle import Vehicle


ref_attr = {
    'bearing': 297,
    'current_status': 'IN_TRANSIT_TO',
    'current_stop_sequence': 4,
    'direction_id': 0,
    'label': '0504',
    'latitude': 42.337215423583984,
    'longitude': -71.10372161865234,
    'speed': None,
    'updated_at': '2019-02-27T10:38:18-05:00'
}
ref_rel = {
    'route': {
        'data': {
            'id': '747',
            'type': 'route'
        }
    },
    'stop': {
        'data': {
            'id': '11803',
            'type': 'stop'
        }
    },
    'trip': {
        'data': {
            'id': '39425386',
            'type': 'trip'
        }
    }
}


class TestVehicle(unittest.TestCase):
    """Tests for `Vehicle` class"""

    def setUp(self):
        self.vehicle = Vehicle('y0504', ref_attr, ref_rel)

    def test_id(self):
        self.assertEqual(self.vehicle.id, 'y0504')

    def test_bearing(self):
        self.assertEqual(self.vehicle.bearing, ref_attr['bearing'])

    def test_status(self):
        self.assertEqual(self.vehicle.status, ref_attr['current_status'])

    def test_stop_seq(self):
        self.assertEqual(
            self.vehicle.stop_sequence,
            ref_attr['current_stop_sequence']
        )

    def test_direction_id(self):
        self.assertEqual(self.vehicle.direction_id, ref_attr['direction_id'])

    def test_latitude(self):
        self.assertEqual(self.vehicle.latitude, ref_attr['latitude'])

    def test_longitude(self):
        self.assertEqual(self.vehicle.longitude, ref_attr['longitude'])

    def test_speed(self):
        self.assertEqual(self.vehicle.speed, ref_attr['speed'])

    def test_updated_at(self):
        self.assertEqual(
            self.vehicle.updated_at,
            parse(ref_attr['updated_at'])
        )

    def test_route(self):
        self.assertEqual(self.vehicle.route, ref_rel['route']['data']['id'])

    def test_stop(self):
        self.assertEqual(self.vehicle.stop, ref_rel['stop']['data']['id'])

    def test_trip(self):
        self.assertEqual(self.vehicle.trip, ref_rel['trip']['data']['id'])

