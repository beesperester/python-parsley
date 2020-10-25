"""Module contains pointer related classes and methods."""


class Pointer(object):
    """Pointer class."""

    def __init__(self, method, argument, path):
        self.method = method
        self.argument = argument
        self.path = path

    def _traverse(self, node, path_parts):
        if not len(path_parts):
            return node

        if isinstance(node, list):
            return [self._traverse(x, path_parts) for x in node]

        part = path_parts[0]
        remaining_parts = path_parts[1:]

        if hasattr(node, part):
            attribute = getattr(node, part)

            if attribute:
                if callable(attribute) and len(remaining_parts):
                    return self._traverse(attribute, remaining_parts)
                else:
                    return attribute

        raise AttributeError(
            "Missing Attribute '{}' in node '{}".format(part, node)
        )

    def serialize(self):
        return {
            "method": self.method,
            "argument": self.argument,
            "path": self.path
        }

    def extract(self, soup):
        argument = self.argument
        path_parts = list(filter(None, self.path.split(".")))
        keyword_arguments = {}

        # account for class selector
        if "." in argument:
            parts = argument.split(".")
            argument = parts[0]
            class_name = ".".join(parts[1:])

            keyword_arguments["class_"] = class_name

        # account for id selector
        elif "#" in argument:
            parts = argument.split("#")
            argument = parts[0]
            id_name = ".".join(parts[1:])

            keyword_arguments["id_"] = id_name

        node = getattr(soup, self.method)(
            argument,
            **keyword_arguments
        )

        return self._traverse(node, path_parts)


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
