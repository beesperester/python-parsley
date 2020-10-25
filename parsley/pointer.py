"""Module contains pointer related classes and methods."""


class Pointer(object):
    """Pointer class."""

    def __init__(self, method, argument, path):
        self.method = method
        self.argument = argument
        self.path = path

    def serialize(self):
        return {
            "method": self.method,
            "argument": self.argument,
            "path": self.path
        }


def create_pointer_from_dict(config):
    """Create Pointer instance from dict."""

    if "method" not in config.keys():
        raise ValueError("Missing 'method' key in config")

    if "argument" not in config.keys():
        raise ValueError("Missing 'argument' key in config")

    if "path" not in config.keys():
        raise ValueError("Missing 'path' key in config")

    method = config["method"]
    argument = config["argument"]
    path = config["path"]

    return Pointer(method, argument, path)


def create_pointer_from_shorthand(config):
    """Create Pointer instance from shorthand string."""

    shorthand_parts = config.split("}")

    method, argument = shorthand_parts[0].strip("{}").split(":")
    path = ".".join(list(filter(None, shorthand_parts[1].split("."))))

    allowed_methods = [
        "find",
        "find_all"
    ]

    if method in allowed_methods:
        return Pointer(method, argument, path)

    raise ValueError("Illegal shorthand format '{}'".format(config))


def create_pointer(config):
    """Create Pointer instance from config dict or shorthand string."""

    if isinstance(config, dict):
        return create_pointer_from_dict(config)

    return create_pointer_from_shorthand(config)
