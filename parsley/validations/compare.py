"""Module contains compare related validation classes and methods."""


from parsley.validations.exceptions import ValidationError
from parsley.validations.validation import ValidationWrapper
from parsley.validations.validations import Validations


def larger_method(key, data, **kwargs):
    if not data > kwargs["value"]:
        raise ValidationError(
            "Field '{}' must be larger than '{}', but is '{}'".format(
                key,
                kwargs["value"],
                data
            )
        )


def smaller_method(key, data, **kwargs):
    if not data < kwargs["value"]:
        raise ValidationError(
            "Field '{}' must be smaller than '{}', but is '{}'".format(
                key,
                kwargs["value"],
                data
            )
        )


def equal_method(key, data, **kwargs):
    if not data == kwargs["value"]:
        raise ValidationError(
            "Field '{}' must be equal '{}', but is '{}'".format(
                key,
                kwargs["value"],
                data
            )
        )


def register():
    validations = Validations()

    compare_larger = ValidationWrapper("compare_larger", larger_method)
    validations.register(compare_larger)

    compare_smaller = ValidationWrapper("compare_smaller", larger_method)
    validations.register(compare_smaller)

    compare_equal = ValidationWrapper("compare_equal", larger_method)
    validations.register(compare_equal)
