"""Test pointer module."""

import unittest

from bs4 import BeautifulSoup

from tests.data import example_source

from parsley.pointer import \
    Pointer, \
    create_pointer, \
    create_pointer_from_dict, \
    create_pointer_from_shorthand


class TestPointerMethods(unittest.TestCase):

    def test_create_pointer_from_dict(self):
        config = {
            "method": "find",
            "argument": "h1.title",
            "path": "text"
        }

        result = create_pointer_from_dict(config)
        expected_result = Pointer("find", "h1.title", "text")

        self.assertDictEqual(
            result.serialize(),
            expected_result.serialize()
        )

    def test_create_pointer_from_shorthand(self):
        config = "{find:h1.title}.text"

        result = create_pointer_from_shorthand(config)
        expected_result = Pointer("find", "h1.title", "text")

        self.assertDictEqual(
            result.serialize(),
            expected_result.serialize()
        )

    def test_pointer_serialize(self):
        config = "{find:h1.title}.text"

        result = create_pointer_from_shorthand(config).serialize()
        expected_result = {
            "method": "find",
            "argument": "h1.title",
            "path": "text"
        }

        self.assertDictEqual(
            result,
            expected_result
        )

    def test_pointer_extract(self):
        soup = BeautifulSoup(example_source, "lxml")
        shorthand = "{find:h1.title}.text"
        pointer = create_pointer_from_shorthand(shorthand)

        result = pointer.extract(soup)
        expected_result = "This is an Example"

        self.assertEqual(
            result,
            expected_result
        )
