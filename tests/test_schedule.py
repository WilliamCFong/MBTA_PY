#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `Schedule` class"""

import unittest
from dateutil.parser import parse
from mbta.schedule.schedule import Schedule
from tests.sample_responses import samp_schedules as samp


class TestSchedule(unittest.TestCase):
    """Tests for `Schedule` class"""

    def setUp(self):
        self.schedules = [Schedule(r['id'], r['attributes'], r['relationships']) for r in samp]
        self.schedule = self.schedules[0]

    def test_id(self):
        self.assertEqual(self.schedule.id, samp[0]['id'])

    def test_arrival_time(self):
        self.assertEqual(
            self.schedule.arrival_time,
            parse(samp[0]['attributes']['arrival_time'])
        )

    def test_departure_time(self):
        self.assertEqual(
            self.schedule.departure_time,
            parse(samp[0]['attributes']['departure_time'])
        )

    def test_drop_off_type(self):
        self.assertEqual(
            self.schedule.drop_off_type,
            samp[0]['attributes']['drop_off_type']
        )

    def test_pickup_type(self):
        self.assertEqual(
            self.schedule.pickup_type,
            samp[0]['attributes']['pickup_type']
        )

    def test_stop_sequence(self):
        self.assertEqual(
            self.schedule.stop_sequence,
            samp[0]['attributes']['stop_sequence']
        )

    def test_timepoint(self):
        self.assertEqual(
            self.schedule.timepoint,
            samp[0]['attributes']['timepoint']
        )

    def test_route(self):
        self.assertEqual(
            self.schedule.route,
            samp[0]['relationships']['route']['data']['id']
        )

    def test_stop(self):
        self.assertEqual(
            self.schedule.stop,
            samp[0]['relationships']['stop']['data']['id']
        )

    def test_trip(self):
        self.assertEqual(
            self.schedule.trip,
            samp[0]['relationships']['trip']['data']['id']
        )
