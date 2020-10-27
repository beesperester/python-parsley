"""Module contains datapoint related classes and methods."""


from parsley.pointer import create_pointer
from parsley.mutations.mutations import create_mutations
from parsley.validations.validations import create_validations


class Datapoint(object):
    """Datapoint class."""

    def __init__(self, name, pointer, mutations=None, validations=None):
        if mutations is None:
            mutations = []

        if validations is None:
            validations = []

        self.name = name
        self.pointer = pointer
        self.mutations = mutations
        self.validations = validations

    def serialize(self):
        return {
            "name": self.name,
            "pointer": self.pointer.serialize(),
            "mutations": [x.serialize() for x in self.mutations],
            "validations": [x.serialize() for x in self.validations]
        }

    def extract(self, soup):
        data = self.pointer.extract(soup)

        for mutation in self.mutations:
            data = mutation.apply(data)

        for validation in self.validations:
            validation.apply(self.name, data)

        return data


def create_datapoint(config):
    """Create Datapoint instance from config dict."""

    name = config["name"]
    pointer = create_pointer(config["pointer"])

    mutations = []
    if "mutations" in config.keys():
        mutations = create_mutations(config["mutations"])

    validations = []
    if "validations" in config.keys():
        validations = create_validations(config["validations"])

    datapoint = Datapoint(
        name,
        pointer,
        mutations,
        validations
    )

    return datapoint
