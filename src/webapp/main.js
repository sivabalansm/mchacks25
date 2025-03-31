/*const options = {
  method: 'POST',
  headers: {
    'Authorization': 'Bearer 800343b91e2a4b0b90b6e84eed644f57',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    "user_id": "twXxG0be3tRDU9MCWUe9nixtBnT2",
    "saved_item_id": "83X4H3uevwRi7YTZWSnx3Q",
    "pipeline_inputs": [{"input_name":"URL","value":"https://www.urbanoutfitters.com/en-ca/shop/emily-icon-ceramic-utensil-holder?category=new-arrivals&color=030&type=REGULAR&viewcode=b&size=ONE+SIZE&quantity=1"}]
  })
};


function temp(run_id) {
const url = 'https://api.gumloop.com/api/v1/get_pl_run?run_id=' + run_id + '&user_id=twXxG0be3tRDU9MCWUe9nixtBnT2';
const headers = {
  Authorization: 'Bearer 800343b91e2a4b0b90b6e84eed644f57',
};

return fetch(url, {
  method: 'GET',
  headers: headers,
})
  .then((response) => response.json())
  .then((data) => console.log(data));
}

let response = fetch('https://api.gumloop.com/api/v1/start_pipeline', options)
  .then(response => temp(respose['run_id']))
  .then(response => console.log(response))
  .catch(err => console.error(err));*/

let response = fetch('http://127.0.0.1:5000/tmp').then(response => console.log(response.json()));
function newProduct(obj) {
	const products = document.getElementsByClassName("products");
	const productToAdd = document.createElement("div");
	productToAdd.innerHTML = 'hehe';
	productToAdd.className = "product";
	products[0].append(productToAdd);
}

document.getElementById("submit").addEventListener('click', function() {
	let inputBox = document.getElementById('newProduct');
	newProduct(inputBox.value);
	inputBox.value = "";
});


