"""Test pointer module."""

import unittest

from parsley.datapoint import \
    Datapoint, \
    create_datapoint
from parsley.pointer import create_pointer_from_shorthand


class TestDatapointMethods(unittest.TestCase):

    def test_create_datapoint(self):
        config = {
            "name": "title",
            "pointer": "{find:h1.title}.text"
        }

        pointer_config = "{find:h1.title}.text"
        pointer = create_pointer_from_shorthand(pointer_config)

        result = create_datapoint(config)
        expected_result = Datapoint("title", pointer)

        self.assertDictEqual(
            result.serialize(),
            expected_result.serialize()
        )
