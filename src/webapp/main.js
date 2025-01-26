let allProducts = [
	{ name: "name",
	price: 33},
];

function newProduct(number) {
	const products = document.getElementsByClassName("products");
	const productToAdd = document.createElement("div");
	productToAdd.innerHTML = number;
	productToAdd.className = "product";
	products[0].append(productToAdd);
}

document.getElementById("submit").addEventListener('click', function() {
	let inputBox = document.getElementById('newProduct');
	newProduct(inputBox.value);
	inputBox.value = "";
});


