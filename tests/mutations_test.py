"""Test schema module."""

import unittest

from parsley.mutations.mutation import Mutation
from parsley.mutations.mutations import create_mutations
from parsley.mutations import string


class TestMutationsMethods(unittest.TestCase):

    def test_create_mutations(self):
        string.register()

        config = [
            {
                "name": "string_replace",
                "find": "foo",
                "replace": "bar"
            }
        ]

        result = create_mutations(config)
        expected_result = [
            Mutation(
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
