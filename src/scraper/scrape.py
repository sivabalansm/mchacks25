from firecrawl import FirecrawlApp
from pydantic import BaseModel
import json

key: str
with open(".env", 'r') as f:
    key = f.read().strip()
print("Your access key:", key)

app = FirecrawlApp(api_key=key)

class NestedModel1(BaseModel):
    name: str
    price: str
    description: str = None

class ExtractSchema(BaseModel):
    clothing_items: list[NestedModel1]

data = app.extract([
  "https://uniqlo.ca/*",
  "https://urbanoutfitters.com/*"
], {
    'prompt': 'Extract all clothing names, prices, and descriptions from the specified websites.',
    'schema': ExtractSchema.model_json_schema(),
})


with open('results.json', 'w') as f:
    f.write(json.dumps(data))


