db = connect("mongodb://root:example0@mongodb:27017/admin");

// Create the `ecommerce` database
db = db.getSiblingDB('ecommerce');

// Optionally, you can create a collection and insert initial data
db.createCollection('products');
db.products.insertMany([
  { name: "Product 1", price: 10.99 },
  { name: "Product 2", price: 19.99 },
]);

print("Initialized 'ecommerce' database with initial data.");
