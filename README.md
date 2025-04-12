# E-commerce Website

This project is a simple Flask-based e-commerce website that allows users to browse and view products. It includes multiple pages and a structured layout for a better user experience.

## Project Structure

```
ecommerce-website
├── templates
│   ├── base.html          # Base template for shared HTML structure
│   ├── home.html          # Home page template
│   ├── products.html      # Template for listing all products
│   └── product_detail.html # Template for displaying product details
├── static
│   ├── css
│   │   └── styles.css     # CSS styles for the website
│   ├── js
│   │   └── scripts.js      # JavaScript for client-side functionality
│   └── images             # Directory for image files
├── app.py                 # Main application file for the Flask app
└── README.md              # Documentation for the project
```

## Features

- Home page with a welcome message and navigation links.
- Product listing page displaying all available products.
- Product detail page showing detailed information about each product.
- Responsive design with CSS for a better user interface.
- JavaScript for dynamic interactions.

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   ```

2. Navigate to the project directory:
   ```
   cd ecommerce-website
   ```

3. Install the required packages:
   ```
   pip install Flask
   ```

4. Run the application:
   ```
   python app.py
   ```

5. Open your web browser and go to `http://127.0.0.1:5000` to view the website.

## Usage

- Visit the home page to explore the site.
- Navigate to the products page to see the list of available products.
- Click on a product to view its details.

## Contributing

Feel free to submit issues or pull requests for improvements and new features!