"""Module contains validation related classes and methods."""


class Validation(object):
    """Validation class."""

    def __init__(self, name, callback, **kwargs):
        self.name = name
        self.callback = callback
        self.arguments = kwargs

    def apply(self, key, data):
        if isinstance(data, list):
            [
                self.callback(key, x, **self.arguments) for x in data
            ]

        self.callback(key, data, **self.arguments)

    def serialize(self):
        return {
            "name": self.name,
            **self.arguments
        }


class ValidationWrapper(object):
    """ValidationWrapper class."""

    def __init__(self, name, callback):
        self.name = name
        self.callback = callback

    def setup(self, **kwargs):
        return Validation(self.name, self.callback, **kwargs)
