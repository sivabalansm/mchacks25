from datetime import timedelta, datetime, date
import matplotlib.pyplot as plt

data = {
        "clothing_items": [
            {
                "name": "hoodie",
                "price": [11, 29, 39, 40],
                "description": "Piece of cloth used to keep one warm"

            }
        ]
}
initial_date = date.today()
dates = [initial_date + timedelta(days=i) for i in range(len(data["clothing_items"][0]["price"]))]

prices = data["clothing_items"][0]["price"]
plt.plot_date(dates, prices, 'g')
print(dates)
plt.show()
