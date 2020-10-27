"""Module contains generic related validation classes and methods."""


from parsley.validations.exceptions import ValidationError
from parsley.validations.validation import ValidationWrapper
from parsley.validations.validations import Validations


def required_method(key, data, **kwargs):
    if not data:
        raise ValidationError("Field '{}' is required".format(key))


def register():
    validations = Validations()

    generic_required = ValidationWrapper("generic_required", required_method)
    validations.register(generic_required)
