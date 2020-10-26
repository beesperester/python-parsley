"""Module contains datapoint related classes and methods."""


from parsley.pointer import create_pointer
from parsley.mutations.mutations import create_mutations


class Datapoint(object):
    """Datapoint class."""

    def __init__(self, name, pointer, mutations=None, validators=None):
        if mutations is None:
            mutations = []

        if validators is None:
            validators = []

        self.name = name
        self.pointer = pointer
        self.mutations = mutations
        self.validators = validators

    def serialize(self):
        return {
            "name": self.name,
            "pointer": self.pointer.serialize(),
            "mutations": [x.serialize() for x in self.mutations],
            "validators": [x.serialize() for x in self.validators]
        }

    def extract(self, soup):
        data = self.pointer.extract(soup)

        for mutation in self.mutations:
            data = mutation.apply(data)

        return data


def create_datapoint(config):
    """Create Datapoint instance from config dict."""

    name = config["name"]
    pointer = create_pointer(config["pointer"])

    mutations = []
    if "mutations" in config.keys():
        mutations = create_mutations(config["mutations"])

    datapoint = Datapoint(
        name,
        pointer,
        mutations,
        config["validators"] if "validators" in config.keys() else None
    )

    return datapoint
