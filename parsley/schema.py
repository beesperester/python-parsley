"""Module contains schema related classes and methods."""

import json

from parsley.datapoint import create_datapoint


class Schema(object):
    """Schema class."""

    def __init__(self, datapoints=None):
        if datapoints is None:
            datapoints = []

        self.datapoints = datapoints

    def apply(self, soup):
        """Apply schema to soup."""

    def serialize(self):
        return [
            x.serialize() for x in self.datapoints
        ]


def create_schema_from_file(file_path):
    """Create Schema instance from file."""

    with open(file_path, "r") as f:
        config = json.load(f)

        return create_schema(config)

    raise IOError("Unable to read file '{}'".format(file_path))


def create_schema(config):
    """Create Schema instance from config dict."""

    datapoints = []

    # for every key and value create datapoint
    for datapoint_config in config:
        datapoint = create_datapoint(datapoint_config)

        datapoints.append(datapoint)

    schema = Schema(datapoints)

    return schema
