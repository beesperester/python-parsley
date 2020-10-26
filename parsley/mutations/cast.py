"""Module contains cast related mutation classes and methods."""


from parsley.mutations.mutation import MutationWrapper
from parsley.mutations.mutations import Mutations


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
    mutations = Mutations()

    cast_float = MutationWrapper("cast_float", cast_float_method)
    mutations.register(cast_float)

    cast_string = MutationWrapper("cast_string", cast_string_method)
    mutations.register(cast_string)

    cast_int = MutationWrapper("cast_int", cast_int_method)
    mutations.register(cast_int)
