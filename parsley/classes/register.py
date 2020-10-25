"""Module contains register related classes and methods."""


class RegisterItemNotFoundError(Exception):
    """Register Item Not Found Error."""


class Register(object):
    """Register class."""

    def __init__(self):
        self.items = []

    def index(self, name):
        try:
            return [x.name for x in self.items].index(name)
        except ValueError:
            pass

        return -1

    def has(self, name):
        return self.index(name) > -1

    def get(self, name):
        if self.has(name):
            return self.items[self.index(name)]

        raise RegisterItemNotFoundError(
            "No item with name '{}'".format(name)
        )

    def register(self, item):
        if not self.has(item.name):
            self.items.append(item)

    def unrergister(self, item_name):
        self.items = [
            x for x in self.items
            if x.name != item_name
        ]
