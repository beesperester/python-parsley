"""Test schema module."""

import unittest

from parsley.datapoint import create_datapoint
from parsley.schema import \
    Schema, \
    create_schema, \
    create_schema_from_file


class TestSchemaMethods(unittest.TestCase):

    def test_create_schema(self):
        config = [
            {
                "name": "title",
                "pointer": "{find:h1.title}.text"
            }
        ]

        datapoints = [
            create_datapoint(
                {
                    "name": "title",
                    "pointer": "{find:h1.title}.text"
                }
            )
        ]

        result = create_schema(config)
        expected_result = Schema(datapoints)

        self.assertListEqual(
            result.serialize(),
            expected_result.serialize()
        )
