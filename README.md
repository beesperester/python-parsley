![Python Package](https://github.com/beesperester/python-parsley/workflows/Python%20Package/badge.svg?branch=main)

# python-parsley
Recipe based scraping of website content. Create recipes for any website and extract any content from the html source in a simple and straig forward matter. Use **transformers** to convert the extracted data in a way most suitable for your further processing.

## Table of contents
1. [Description](#description)
1. [Example](#example)
1. [Transformers](#transformers)

## Description

Detailed description needs to be written.

## Example

This is your basic recipe json-file. It contains all the datapoints you want to extract.

> /path/to/config.json

```json
[
    {
        "name": "title",
        "pointer": "{find:h1.title}.text",
        "transformers": [
            {
                "name": "string_replace",
                "find": "an Example",
                "replace": "awesome"
            }
        ]
    }
]
```

This is an example usecase using a mockup html markug.

> example.py

```python
from bs4 import BeautifulSoup

# import create_schema and string transformers
from parsley.schema import create_schema_from_file
from parsley.transformers import string

# register string transformers
string.register()

# create schema from json file
schema = create_schema_from_file("/path/to/config.json")

# create html example mockup
example_source = (
    "<html>"
    "<head>"
    "<title>Example</title>"
    "</head>"
    "<body>"
    "<h1 class=\"title\">This is an Example</h1>"
    "</body>"
    "</html>"
)

soup = BeautifulSoup(example_source, "lxml")

# apply schema to soup
data = schema.apply(soup)

print(data)
# prints: 'This is awesome'
```

## Transformers

### String

**string_replace**

Find value in string and replace with new value.

```json
{
    "name": "string_replace",
    "find": "value_to_find",
    "replace": "value_to_replace
}
```

**string_split**

Split string at delimiter and return list.

```json
{
    "name": "string_split",
    "delimiter": ","
}
```

**string_strip**

Strip whitespace from input.

```json
{
    "name": "string_strip"
}
```

### Cast

**cast_float**

Cast input to float.

```json
{
    "name": "cast_float"
}
```

**cast_int**

Cast input to int.

```json
{
    "name": "cast_int"
}
```

**cast_string**

Cast input to string.

```json
{
    "name": "cast_string"
}
```

### Math

**math_multiply**

Multiply input by value.

```json
{
    "name": "math_multiply",
    "value": 2
}
```