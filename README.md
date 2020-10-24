# python-parsley
Recipe based scraping of website content

```python
from parsley.schema import create_schema

schema = create_schema("/path/to/config.json")

data = schema.apply("http://www.example.com)
```