import requests
import json
from time import sleep

url = "https://api.gumloop.com/api/v1/start_pipeline"

payload = {
  "user_id": "twXxG0be3tRDU9MCWUe9nixtBnT2",
  "saved_item_id": "83X4H3uevwRi7YTZWSnx3Q",
  "pipeline_inputs": [{"input_name":"URL","value":"https://www.urbanoutfitters.com/en-ca/shop/emily-icon-ceramic-utensil-holder?category=new-arrivals&color=030&type=REGULAR&viewcode=b&size=ONE+SIZE&quantity=1"}]
}
headers = {
  "Authorization": "Bearer 800343b91e2a4b0b90b6e84eed644f57",
  "Content-Type": "application/json"
}

response = requests.request("POST", url, json=payload, headers=headers)

response_json = json.loads(response.text)
sleep(15)
url = f"https://api.gumloop.com/api/v1/get_pl_run?run_id={response_json["run_id"]}&user_id={payload["user_id"]}"
headers = {
    "Authorization": "Bearer 800343b91e2a4b0b90b6e84eed644f57"
}

response = requests.get(url, headers=headers)
print(response.json()['outputs'])


from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)


# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.

@app.route("/tmp")
def temp():
    return jsonify(response.json()['outputs'])
    

if __name__ == '__main__':
    app.run()
