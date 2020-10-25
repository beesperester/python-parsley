"""Module contains transformers related classes and methods."""


from parsley.classes.register import Register
from parsley.transformers.string import string_replace


def register():
    TRANSFORMERS.register(string_replace)


def create_transformers(config):
    """Create transformser from config list."""

    transformers = []

    for transformer_config in config:
        transformer_name = transformer_config["name"]
        if TRANSFORMERS.has(transformer_name):
            transformer = TRANSFORMERS.get(transformer_name)

            del transformer_config["name"]

            transformers.append(
                transformer.setup(**transformer_config)
            )

    return transformers


TRANSFORMERS = Register()
