"""Module contains string related transformer classes and methods."""


from parsley.transformers.transformer import TransformerWrapper
from parsley.transformers.transformers import TRANSFORMERS


def replace_method(data, **kwargs):
    if isinstance(data, str):
        return data.replace(kwargs["find"], kwargs["replace"])

    raise TypeError(
        "Type must be 'str' but is '{}'".format(
            type(data).__class__
        )
    )


def split_method(data, **kwargs):
    if isinstance(data, str):
        return data.split(kwargs["delimiter"])

    raise TypeError(
        "Type must be 'str' but is '{}'".format(
            type(data).__class__
        )
    )


def strip_method(data, **kwargs):
    if isinstance(data, str):
        return data.strip()

    raise TypeError(
        "Type must be 'str' but is '{}'".format(
            type(data).__class__
        )
    )


def register():
    string_replace = TransformerWrapper("string_replace", replace_method)
    TRANSFORMERS.register(string_replace)

    string_split = TransformerWrapper("string_split", split_method)
    TRANSFORMERS.register(string_split)

    string_strip = TransformerWrapper("string_strip", strip_method)
    TRANSFORMERS.register(string_strip)
