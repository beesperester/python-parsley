"""Module contains mutation related classes and methods."""


class Mutation(object):
    """Mutation class."""

    def __init__(self, name, callback, **kwargs):
        self.name = name
        self.callback = callback
        self.arguments = kwargs

    def apply(self, data):
        if isinstance(data, list):
            return [
                self.callback(x, **self.arguments) for x in data
            ]

        return self.callback(data, **self.arguments)

    def serialize(self):
        return {
            "name": self.name,
            **self.arguments
        }


class MutationWrapper(object):
    """MutationWrapper class."""

    def __init__(self, name, callback):
        self.name = name
        self.callback = callback

    def setup(self, **kwargs):
        return Mutation(self.name, self.callback, **kwargs)
