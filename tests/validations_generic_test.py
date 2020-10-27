"""Test validations generic module."""

import unittest

from parsley.validations.validation import Validation
from parsley.validations.validations import create_validations
from parsley.validations.exceptions import ValidationError
from parsley.validations.generic import required_method


class TestValidationsGenericMethods(unittest.TestCase):

    def test_required_method_fails(self):
        self.assertRaises(
            ValidationError,
            required_method,
            "field",
            None
        )

    def test_required_method_succeeds(self):
        required_method("field", "hello world")
