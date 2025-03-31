import json
from random import randint

data: dict
with open('results.json', 'r') as f:
    data = json.loads(f.read())
list_of_items = data[0]['clothing_items']
for idx, item in enumerate(list_of_items):
    base_price = list_of_items[idx]['price']
    list_of_items[idx]['price'] = [base_price + randint(-10, 10) for _ in range(randint(3, 15))]

print(data)
with open("results_simulated.json", "w") as f:
    f.write(json.dumps(data))





