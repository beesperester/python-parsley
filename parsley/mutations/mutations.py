"""Module contains mutations related classes and methods."""


from parsley.classes.register import Register
from parsley.classes.singleton import Singleton


class Mutations(Singleton, Register):
    """Mutations class."""

    items = []

    def __init__(self):
        pass
