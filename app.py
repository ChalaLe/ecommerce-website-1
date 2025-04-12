from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Sample product data
products = [
    {"id": 1, "name": "Coffee Beans", "price": 200, "category": "Beverages", "description": "Freshly roasted coffee beans."},
    {"id": 2, "name": "Injera", "price": 50, "category": "Food", "description": "Traditional Ethiopian flatbread."},
    {"id": 3, "name": "Ethiopian Spices", "price": 100, "category": "Spices", "description": "A mix of authentic Ethiopian spices."},
    {"id": 4, "name": "Teff Flour", "price": 80, "category": "Food", "description": "Gluten-free flour made from teff."},
    {"id": 5, "name": "Berbere Spice Mix", "price": 120, "category": "Spices", "description": "A spicy blend of Ethiopian spices."},
]

# Home route
@app.route('/')
def home():
    return render_template('home.html')

# Get all products
@app.route('/products', methods=['GET'])
def get_products():
    return render_template('products.html', products=products)

# Get product by ID
@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = next((p for p in products if p["id"] == product_id), None)
    if product:
        return render_template('product_detail.html', product=product)
    return jsonify({"error": "Product not found"}), 404

# Add a new product
@app.route('/products', methods=['POST'])
def add_product():
    new_product = request.json
    new_product["id"] = len(products) + 1
    products.append(new_product)
    return jsonify(new_product), 201

if __name__ == '__main__':
    app.run(debug=True)