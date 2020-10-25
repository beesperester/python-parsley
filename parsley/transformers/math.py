"""Module contains math related transformer classes and methods."""


from parsley.transformers.transformer import TransformerWrapper
from parsley.transformers.transformers import TRANSFORMERS


def math_multiply_method(data, **kwargs):
    if isinstance(data, (str, int, float)):
        return data * kwargs["value"]

    raise TypeError(
        "Type must be 'str|int|float' but is '{}'".format(
            type(data).__class__
        )
    )


def register():
    math_multiply = TransformerWrapper("math_multiply", math_multiply_method)
    TRANSFORMERS.register(math_multiply)
