"""Module contains datapoint related classes and methods."""


from parsley.pointer import create_pointer


class Datapoint(object):
    """Datapoint class."""

    def __init__(self, name, pointer, transformers=None, validators=None):
        if transformers is None:
            transformers = []

        if validators is None:
            validators = []

        self.name = name
        self.pointer = pointer
        self.transformers = transformers
        self.validators = validators

    def serialize(self):
        return {
            "name": self.name,
            "pointer": self.pointer.serialize(),
            "transformers": [x.serialize() for x in self.transformers],
            "validators": [x.serialize() for x in self.validators]
        }


def create_datapoint(config):
    """Create Datapoint instance from config dict."""

    name = config["name"]
    pointer = create_pointer(config["pointer"])

    datapoint = Datapoint(
        name,
        pointer,
        config["transformers"] if "transformers" in config.keys() else None,
        config["validators"] if "validators" in config.keys() else None
    )

    return datapoint
