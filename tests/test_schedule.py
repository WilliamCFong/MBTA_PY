#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `Schedule` class"""

import unittest
from dateutil.parser import parse
from mbta.schedule.schedule import Schedule


ref_attr = {
    'arrival_time': '2019-02-27T05:55:00-05:00',
    'departure_time': '2019-02-27T05:55:00-05:00',
    'drop_off_type': 1,
    'pickup_type': 0,
    'stop_sequence': 1,
    'timepoint': True
}

ref_rel = {
    'prediction': {},
    'route': {
        'data': {
            'id': '747',
            'type': 'route'
        }
    },
    'stop': {
        'data': {
            'id': '17863',
            'type': 'stop'
        }
    },
    'trip': {
        'data': {
            'id': '394424601',
            'type': 'trip'
        }
    }
}

class TestSchedule(unittest.TestCase):
    """Tests for `Schedule` class"""

    def setUp(self):
        self.schedule = Schedule(
            'schedule-394424601-17863-1',
            ref_attr,
            ref_rel
        )

    def test_id(self):
        self.assertEqual(self.schedule.id, 'schedule-394424601-17863-1')

    def test_arrival_time(self):
        self.assertEqual(
            self.schedule.arrival_time,
            parse(ref_attr['arrival_time'])
        )

    def test_departure_time(self):
        self.assertEqual(
            self.schedule.departure_time,
            parse(ref_attr['departure_time'])
        )

    def test_drop_off_type(self):
        self.assertEqual(
            self.schedule.drop_off_type,
            ref_attr['drop_off_type']
        )

    def test_pickup_type(self):
        self.assertEqual(
            self.schedule.pickup_type,
            ref_attr['pickup_type']
        )

    def test_stop_sequence(self):
        self.assertEqual(
            self.schedule.stop_sequence,
            ref_attr['stop_sequence']
        )

    def test_timepoint(self):
        self.assertEqual(
            self.schedule.timepoint,
            ref_attr['timepoint']
        )

    def test_route(self):
        self.assertEqual(
            self.schedule.route,
            ref_rel['route']['data']['id']
        )

    def test_stop(self):
        self.assertEqual(
            self.schedule.stop,
            ref_rel['stop']['data']['id']
        )

    def test_trip(self):
        self.assertEqual(
            self.schedule.trip,
            ref_rel['trip']['data']['id']
        )
