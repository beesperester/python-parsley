"""Test validations compare module."""

import unittest

from parsley.validations.validation import Validation
from parsley.validations.validations import create_validations
from parsley.validations.exceptions import ValidationError
from parsley.validations.compare import \
    larger_method, \
    smaller_method, \
    equal_method


class TestValidationsCompareMethods(unittest.TestCase):

    def test_larger_method_fails(self):
        self.assertRaises(ValidationError, larger_method, "field", 0, value=5)

    def test_larger_method_succeeds(self):
        larger_method("field", 5, value=0)

    def test_smaller_method_fails(self):
        self.assertRaises(ValidationError, smaller_method, "field", 5, value=0)

    def test_smaller_method_succeeds(self):
        smaller_method("field", 0, value=5)

    def test_equal_method_fails(self):
        self.assertRaises(ValidationError, equal_method, "field", 1, value=0)

    def test_equal_method_succeeds(self):
        equal_method("field", 1, value=1)
