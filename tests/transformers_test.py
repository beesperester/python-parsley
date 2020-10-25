"""Test schema module."""

import unittest

from parsley.transformers.transformer import Transformer
from parsley.transformers.transformers import \
    create_transformers, \
    register


class TestTransformersMethods(unittest.TestCase):

    def test_create_transformers(self):
        register()

        config = [
            {
                "name": "string_replace",
                "find": "foo",
                "replace": "bar"
            }
        ]

        result = create_transformers(config)
        expected_result = [
            Transformer(
                "string_replace",
                None,
                find="foo",
                replace="bar"
            )
        ]

        self.assertListEqual(
            [x.serialize() for x in result],
            [x.serialize() for x in expected_result]
        )
