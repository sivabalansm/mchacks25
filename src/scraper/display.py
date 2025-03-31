from datetime import timedelta, datetime, date
import json
import matplotlib.pyplot as plt
from random import sample

def random_items(num: int, data):
    return sample(data[0]["clothing_items"], num)

data = {
        "clothing_items": [
            {
                "name": "hoodie",
                "price": [11, 29, 39, 40],
                "description": "Piece of cloth used to keep one warm"

            }
        ]
}
with open("results_simulated.json", "r") as f:
    data = json.loads(f.read())

def create_subplot(subplot, item: dict):

    initial_date = date.today()
    dates = [initial_date + timedelta(days=i) for i in range(len(item["price"]))]
    prices = item["price"]
    subplot.set_title(item["name"])
    subplot.plot_date(dates, prices, 'b')



PLOT_COUNT = 7
fig, axs = plt.subplots(PLOT_COUNT)
fig.tight_layout()

list_of_items = data[0]["clothing_items"]
list_of_items = random_items(PLOT_COUNT, data)
for i in range(PLOT_COUNT):
    create_subplot(axs[i], list_of_items[i])

plt.show()
