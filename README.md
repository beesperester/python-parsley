# python-parsley
Recipe based scraping of website content

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