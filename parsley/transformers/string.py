"""Module contains string related transformer classes and methods."""


from parsley.transformers.transformer import TransformerWrapper


def replace_method(data, **kwargs):
    if isinstance(data, str):
        return data.replace(kwargs["find"], kwargs["replace"])

    raise TypeError(
        "Type must be 'str' but is '{}'".format(
            type(data).__class__
        )
    )


string_replace = TransformerWrapper("string_replace", replace_method)
