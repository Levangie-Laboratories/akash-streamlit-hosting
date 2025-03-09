# Streamlit E-Commerce Application

## Overview
This is a feature-rich e-commerce application built with Streamlit. It provides a complete shopping experience with product browsing, cart management, and checkout functionality. The application demonstrates how Streamlit can be used to create interactive web applications with minimal code.

## Features

### Product Browsing
- Interactive product catalog with details and images
- Category filtering to narrow down product selection
- Search functionality to find specific products
- Product cards with ratings, pricing, and feature highlights
- Discount indicators for sale items

### Shopping Experience
- Add products to cart with quantity control
- Wishlist functionality to save products for later
- Responsive layout with interactive elements
- Product ratings and reviews display

### Cart Management
- Cart overview with product thumbnails
- Quantity adjustment controls
- Subtotal calculation per item
- Clear and intuitive interface

### Checkout Process
- Order summary with subtotal, shipping, and tax calculations
- Free shipping threshold notification
- Order confirmation with order number
- Simulated checkout process

## Project Structure
```
.
├── app/
│   ├── app.py          # Main application file
│   ├── products.py     # Product catalog data
│   └── requirements.txt # Python dependencies
└── README.md          # This file
```

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/streamlit-ecommerce.git
cd streamlit-ecommerce
```

2. Install the required dependencies:
```bash
pip install -r app/requirements.txt
```

## Usage

1. Start the Streamlit application:
```bash
streamlit run app/app.py
```

2. Open your web browser and navigate to http://localhost:8501

3. Browse the product catalog, add items to your cart, and explore the features!

## Customization

### Adding Products
You can add more products by editing the `products.py` file. Each product should include:
- ID
- Name
- Price and original price (for discounts)
- Description
- Image URL
- Category
- Rating and review count
- Features list

### Modifying Categories
The application uses predefined categories that can be edited in the `products.py` file. Adding a new category is as simple as adding it to the categories list.

## Technologies Used

- **Streamlit**: Powers the interactive web application
- **Pandas**: For data manipulation and display
- **Python 3.9+**: Core programming language
- **Custom CSS**: For styling and layout enhancements

## Future Improvements

- User authentication and accounts
- Persistent storage for orders and user data
- Payment processing integration
- Product recommendations
- Enhanced mobile responsiveness

## License

This project is open source and available under the [MIT License](LICENSE).
