"""Module contains mutations related classes and methods."""


from parsley.classes.register import Register
from parsley.classes.singleton import Singleton


class Mutations(Singleton, Register):
    """Mutations class."""

    items = []

    def __init__(self):
        pass


def create_mutations(config):
    """Create mutations from config list."""

    mutations = Mutations()
    applicable_mutations = []

    for mutation_config in config:
        mutation_name = mutation_config["name"]
        if mutations.has(mutation_name):
            mutation_wrapper = mutations.get(mutation_name)

            del mutation_config["name"]

            applicable_mutations.append(
                mutation_wrapper.setup(**mutation_config)
            )

    return applicable_mutations
