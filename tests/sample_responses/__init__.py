import json
import os


class Sample:
    """A helper class for managing static sample JSON returns from MBTA API V3.
    """

    def __init__(self, json_path):
        self.raw_json = json.loads(open(json_path, 'rt').read())

    def __repr__(self):
        return self.raw_json['data']

    def __str__(self):
        return self.raw_json['data']

    def __getitem__(self, key):
        return self.raw_json['data'][key]

BASE = os.path.dirname(os.path.abspath(__name__))
BASE = os.path.join(BASE, 'tests', 'sample_responses')

samp_predictions = Sample(os.path.join(BASE, 'predictions.json'))
samp_schedules = Sample(os.path.join(BASE, 'schedules.json'))

del BASE
