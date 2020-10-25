"""Module contains cast related transformer classes and methods."""


from parsley.transformers.transformer import TransformerWrapper
from parsley.transformers.transformers import TRANSFORMERS


def cast_float_method(data, **kwargs):
    if isinstance(data, (str, int, float)):
        return float(data)

    raise TypeError(
        "Type must be 'str|int|float' but is '{}'".format(
            type(data).__class__
        )
    )


def cast_string_method(data, **kwargs):
    if isinstance(data, (str, int, float)):
        return str(data)

    raise TypeError(
        "Type must be 'str|int|float' but is '{}'".format(
            type(data).__class__
        )
    )


def cast_int_method(data, **kwargs):
    if isinstance(data, (str, int, float)):
        return int(data)

    raise TypeError(
        "Type must be 'str|int|float' but is '{}'".format(
            type(data).__class__
        )
    )


def register():
    cast_float = TransformerWrapper("cast_float", cast_float_method)
    TRANSFORMERS.register(cast_float)

    cast_string = TransformerWrapper("cast_string", cast_string_method)
    TRANSFORMERS.register(cast_string)

    cast_int = TransformerWrapper("cast_int", cast_int_method)
    TRANSFORMERS.register(cast_int)
