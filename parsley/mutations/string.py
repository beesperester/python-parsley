"""Module contains string related mutation classes and methods."""


from parsley.mutations.mutation import MutationWrapper
from parsley.mutations.mutations import Mutations


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
    mutations = Mutations()

    string_replace = MutationWrapper("string_replace", replace_method)
    mutations.register(string_replace)

    string_split = MutationWrapper("string_split", split_method)
    mutations.register(string_split)

    string_strip = MutationWrapper("string_strip", strip_method)
    mutations.register(string_strip)
