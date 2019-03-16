#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `prediction` object."""

import unittest
import json
from dateutil.parser import parse
from unittest.mock import patch
from mbta.prediction.prediction import Prediction
from tests.sample_responses import samp_predictions as samp


class TestPrediction(unittest.TestCase):
    """Unit tests for the Prediction class."""

    def setUp(self):
        self.predictions = [Prediction(p['id'], p['attributes'], p['relationships']) for p in samp]
        self.prediction = self.predictions[0]

    def test_id(self):
        self.assertEqual(self.prediction.id, samp[0]['id'])

    def test_stop_sequence(self):
        self.assertEqual(
            self.prediction.stop_sequence,
            samp[0]['attributes']['stop_sequence']
        )

    def test_status(self):
        self.assertEqual(
            self.prediction.status,
            samp[0]['attributes']['status']
        )

    def test_direction_id(self):
        self.assertEqual(
            self.prediction.direction_id,
            samp[0]['attributes']['direction_id']
        )

    def test_departure_time(self):
        if samp[0]['attributes']['departure_time']:
            self.assertEqual(
                self.prediction.departure_time,
                parse(samp[0]['attributes']['departure_time'])
            )
        else:
            self.assertEqual(self.prediction.departure_time, None)

    def test_arrival_time(self):
        if samp[0]['attributes']['arrival_time']:
            self.assertEqual(
                self.prediction.arrival_time,
                parse(samp[0]['attributes']['arrival_tim'])
            )
        else:
            self.assertEqual(self.prediction.arrival_time, None)
