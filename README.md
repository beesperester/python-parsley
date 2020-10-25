# python-parsley
Recipe based scraping of website content

![Python Package](https://github.com/beesperester/python-parsley/workflows/Python%20Package/badge.svg?branch=main)

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
from bs4 import BeautifulSoup
from parsley.schema import create_schema

schema = create_schema_from_file("/path/to/config.json")

source = "<html><head><title>Example</title></head><body><h1 class=\"title\">This is an Example</h1></body></html>"

soup = BeautifulSoup(source, "lxml")

data = schema.apply(soup)
```