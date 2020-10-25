"""Module contains transformer related classes and methods."""


class Transformer(object):
    """Transformer class."""

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


class TransformerWrapper(object):
    """TransformerWrapper class."""

    def __init__(self, name, callback):
        self.name = name
        self.callback = callback

    def setup(self, **kwargs):
        return Transformer(self.name, self.callback, **kwargs)
