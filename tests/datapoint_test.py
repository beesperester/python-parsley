"""Test pointer module."""

import unittest

from bs4 import BeautifulSoup

from data import example_source

from parsley.datapoint import \
    Datapoint, \
    create_datapoint
from parsley.pointer import create_pointer_from_shorthand
from parsley.transformers import string


class TestDatapointMethods(unittest.TestCase):

    def test_create_datapoint(self):
        pointer_config = "{find:h1.title}.text"
        pointer = create_pointer_from_shorthand(pointer_config)

        config = {
            "name": "title",
            "pointer": "{find:h1.title}.text"
        }

        result = create_datapoint(config)
        expected_result = Datapoint("title", pointer)

        self.assertDictEqual(
            result.serialize(),
            expected_result.serialize()
        )

    def test_datapoint_serialize(self):
        pointer_config = "{find:h1.title}.text"
        pointer = create_pointer_from_shorthand(pointer_config)

        config = {
            "name": "title",
            "pointer": "{find:h1.title}.text"
        }

        result = create_datapoint(config).serialize()
        expeced_result = {
            "name": "title",
            "pointer": {
                "method": "find",
                "argument": "h1.title",
                "path": "text"
            },
            "transformers": [],
            "validators": []
        }

        self.assertDictEqual(
            result,
            expeced_result
        )

    def test_datapoint_extract(self):
        string.register()

        soup = BeautifulSoup(example_source, "lxml")

        config = {
            "name": "title",
            "pointer": "{find:h1.title}.text",
            "transformers": [
                {
                    "name": "string_replace",
                    "find": "an Example",
                    "replace": "awesome"
                }
            ]
        }

        datapoint = create_datapoint(config)

        result = datapoint.extract(soup)
        expected_result = "This is awesome"

        self.assertEqual(
            result,
            expected_result
        )
