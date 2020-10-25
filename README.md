# python-parsley
Recipe based scraping of website content

![Python Package](https://github.com/beesperester/python-parsley/workflows/Python%20Package/badge.svg?branch=main)

/path/to/config.json
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

example.py
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