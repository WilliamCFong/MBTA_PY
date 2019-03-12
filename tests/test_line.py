#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `Line` class"""

import unittest
from mbta.line.line import Line

ref_attr = {
    'color': 'DA291C',
    'long_name': 'Red Line',
    'short_name': '',
    'sort_order': 10010,
    'text_color': 'FFFFFF'
}

class TestLine(unittest.TestCase):
    """Unit tests for `Line` class"""

    def setUp(self):
        self.line = Line('line-Red', ref_attr)

    def test_id(self):
        self.assertEqual(self.line.id, 'line-Red')

    def test_color(self):
        self.assertEqual(self.line.color, ref_attr['color'])

    def test_text_color(self):
        self.assertEqual(self.line.text_color, ref_attr['text_color'])

    def test_long_name(self):
        self.assertEqual(self.line.long_name, ref_attr['long_name'])

    def test_short_name(self):
        self.assertEqual(self.line.short_name, ref_attr['short_name'])

    def test_sort_order(self):
        self.assertEqual(self.line.sort_order, ref_attr['sort_order'])
