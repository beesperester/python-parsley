"""Module contains math related mutation classes and methods."""


from parsley.mutations.mutation import MutationWrapper
from parsley.mutations.mutations import Mutations


def math_multiply_method(data, **kwargs):
    if isinstance(data, (str, int, float)):
        return data * kwargs["value"]

    raise TypeError(
        "Type must be 'str|int|float' but is '{}'".format(
            type(data).__class__
        )
    )


def register():
    mutations = Mutations()

    math_multiply = MutationWrapper("math_multiply", math_multiply_method)
    mutations.register(math_multiply)
