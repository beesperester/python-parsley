"""Module contains validations related classes and methods."""


from parsley.classes.register import Register
from parsley.classes.singleton import Singleton

from parsley.validations.exceptions import MissingValidationError


class Validations(Singleton, Register):
    """Validations class."""

    items = []

    def __init__(self):
        pass


def create_validations(config):
    """Create validations from config list."""

    validations = Validations()
    applicable_validations = []

    for validation_config in config:
        validation_name = validation_config["name"]
        if validations.has(validation_name):
            validation_wrapper = validations.get(validation_name)

            del validation_config["name"]

            applicable_validations.append(
                validation_wrapper.setup(**validation_config)
            )
        else:
            raise MissingValidationError(
                "Missing validation '{}'".format(validation_name)
            )

    return applicable_validations
