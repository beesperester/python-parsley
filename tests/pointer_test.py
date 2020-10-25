"""Test pointer module."""

import unittest

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
