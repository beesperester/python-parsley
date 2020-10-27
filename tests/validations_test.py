"""Test validations module."""

import unittest

from parsley.validations.validation import Validation
from parsley.validations.validations import create_validations
from parsley.validations import string


class TestValidationsMethods(unittest.TestCase):

    def test_create_validations(self):
        string.register()

        config = [
            {
                "name": "generic_required"
            }
        ]

        result = create_validations(config)
        expected_result = [
            Validation(
                "generic_required",
                None
            )
        ]

        self.assertListEqual(
            [x.serialize() for x in result],
            [x.serialize() for x in expected_result]
        )
