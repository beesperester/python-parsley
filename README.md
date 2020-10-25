# python-parsley
Recipe based scraping of website content

![Python package](https://github.com/beesperester/python-parsley/workflows/Python%20package/badge.svg?branch=main)

**/path/to/config.json**
```json
[
    {
        "name": "title",
        "pointer": "{find:h1.title}.text
    }
]
```

```python
from parsley.schema import create_schema

schema = create_schema_from_file("/path/to/config.json")

data = schema.apply(soup)
```