#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `mbta` package."""


import unittest
from click.testing import CliRunner

from mbta import mbta
from mbta.mbta import MBTA
from mbta import cli


class TestMbta(unittest.TestCase):
    """Tests for `mbta` package."""

    def setUp(self):
        """Set up test fixtures, if any."""
        self.mbta = MBTA('secret')

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'mbta.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output
