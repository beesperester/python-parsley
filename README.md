![Python Package](https://github.com/beesperester/python-parsley/workflows/Python%20Package/badge.svg?branch=main)

# python-parsley
Recipe based scraping of website content. 

Create recipes for any website and extract any content from the html source in a simple and straightforward matter. Use **mutations** to convert the extracted data in a way most suitable for your further processing.

## Table of contents
1. [Description](#description)
1. [Example](#example)
1. [Mutations](#mutations)
    * [String](#string)
    * [Cast](#cast)
    * [Math](#math)
    * [Extending](#extending-mutations)
1. [Validations](#validations)
    * [Generic](#generic)
    * [Compare](#compare)
    * [Extending](#extending-validations)

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
        "mutations": [
            {
                "name": "string_replace",
                "find": "an Example",
                "replace": "awesome"
            }
        ],
        "validations": [
            {
                "name": "generic_required"
            }
        ]
    }
]
```

This is an example usecase using a mockup html markup.

> example.py

```python
from bs4 import BeautifulSoup

# import create_schema and string mutations
from parsley.schema import create_schema_from_file
from parsley.mutations import string
from parsley.validations import generic

# register string mutations
string.register()

# register generic validations
generic.register()

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

## Mutations

Mutations are small functions that process the extracted data in the order they are set up. This makes it easy to grab &ndash; for example &ndash; a string value, strip away whitespace and cast it into a float.

Mutations work on either single data points or lists, where every mutation will be applied to each item in the list.

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

### Extending Mutations

You can add your own mutations.

```python
from parsley.mutations.mutation import MutationWrapper
from parsley.mutations.mutations import Mutations

# get mutations singleton instance
mutations = Mutations()

# create mutations callback
# first argument is the data which will be mutated
# second argument can be any extra key value pair from the config
def my_callback(data, **kwargs):
    # do something to the data
    if isinstance(data, str):
        return data.lower()

    raise Exception("Input must be of type 'str'")

# create mutation wrapper
# first argument is the key by which it can be used from the config
# second argument is the method that should be called
my_mutation = MutationWrapper("my_mutation", my_callback)

# register your mutation with the mutations singleton
mutations.register(my_mutation)
```

## Validations

Validations are small functions for checking if the extracted data matches the criteria described in the schema config.

### Generic

**generic_required**

Input is required.

```json
{
    "name": "generic_required"
}
```

### Compare

**compare_larger**

Input must be larger than value.

```json
{
    "name": "compare_larger",
    "value": 0
}
```

**compare_smaller**

Input must be smaller than value.

```json
{
    "name": "compare_smaller",
    "value": 1000.0
}
```

**compare_equal**

Input must be equal to value.

```json
{
    "name": "compare_equal",
    "value": 0
}
```

### Extending Validations

You can add your own validations.

```python
from parsley.validations.validation import ValidationWrapper
from parsley.validations.validations import Validations
from parsley.validations.exceptions import ValidationError

# get validations singleton instance
validations = Validations()

# create validations callback
# first argument is the name of the input
# second argument is the data which will be mutated
# third argument can be any extra key value pair from the config
def my_callback(key, data, **kwargs):
    # do something to the data
    if not isinstance(data, str):
        raise ValidationError("Input must be of type 'str'")

# create validation wrapper
# first argument is the key by which it can be used from the config
# second argument is the method that should be called
my_validation = ValidationWrapper("my_validation", my_callback)

# register your validation with the validations singleton
validations.register(my_validation)
```