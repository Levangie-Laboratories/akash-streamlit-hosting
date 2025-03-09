import streamlit as st
import pandas as pd
import time
from products import products, categories

# Page configuration
st.set_page_config(page_title="E-Commerce Store", page_icon="🛒", layout="wide")

# Custom CSS for styling
st.markdown(
    """
<style>
    /* Main styles */
    .main {
        background-color: #f8f9fa;
    }
    
    /* Header styling */
    .header-container {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 1rem 0;
        border-bottom: 1px solid #eee;
        margin-bottom: 2rem;
    }
    
    .site-title {
        font-size: 2rem;
        font-weight: 700;
        color: #333;
        margin: 0;
    }
    
    /* Product card styling */
    .product-card {
        border-radius: 10px;
        padding: 1rem;
        margin-bottom: 1rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        transition: transform 0.2s, box-shadow 0.2s;
        background-color: white;
    }
    
    .product-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
    }
    
    .product-title {
        font-size: 1.2rem;
        font-weight: 600;
        margin-top: 0.5rem;
    }
    
    .price-tag {
        font-size: 1.25rem;
        font-weight: 600;
        color: #2e7d32;
    }
    
    .original-price {
        text-decoration: line-through;
        color: #757575;
        margin-left: 0.5rem;
    }
    
    .discount-badge {
        background-color: #e53935;
        color: white;
        padding: 0.25rem 0.5rem;
        border-radius: 4px;
        font-size: 0.75rem;
        font-weight: 600;
    }
    
    .rating-container {
        display: flex;
        align-items: center;
        margin: 0.5rem 0;
    }
    
    .rating-stars {
        color: #ffc107;
        margin-right: 0.5rem;
    }
    
    .review-count {
        color: #757575;
        font-size: 0.85rem;
    }
    
    .feature-tag {
        display: inline-block;
        background-color: #e3f2fd;
        color: #1565c0;
        padding: 0.25rem 0.5rem;
        border-radius: 4px;
        font-size: 0.75rem;
        margin-right: 0.5rem;
        margin-bottom: 0.5rem;
    }
    
    /* Button styling */
    .add-to-cart-btn {
        background-color: #1976d2;
        color: white;
        border: none;
        padding: 0.5rem 1rem;
        border-radius: 4px;
        cursor: pointer;
        width: 100%;
        font-weight: 600;
        margin-top: 0.5rem;
    }
    
    .add-to-cart-btn:hover {
        background-color: #1565c0;
    }
    
    .wishlist-btn {
        background-color: white;
        color: #e53935;
        border: 1px solid #e53935;
        padding: 0.5rem 1rem;
        border-radius: 4px;
        cursor: pointer;
        width: 100%;
        font-weight: 600;
        margin-top: 0.5rem;
    }
    
    .wishlist-btn:hover {
        background-color: #ffebee;
    }
    
    /* Cart styling */
    .cart-item {
        display: flex;
        align-items: center;
        padding: 1rem;
        margin-bottom: 1rem;
        border-radius: 8px;
        background-color: white;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    
    .cart-item-image {
        width: 80px;
        height: 80px;
        object-fit: cover;
        border-radius: 4px;
        margin-right: 1rem;
    }
    
    .cart-item-details {
        flex: 1;
    }
    
    .cart-item-title {
        font-size: 1.1rem;
        font-weight: 600;
        margin: 0;
    }
    
    .cart-item-price {
        color: #2e7d32;
        font-weight: 600;
        margin: 0.25rem 0;
    }
    
    .quantity-control {
        display: flex;
        align-items: center;
    }
    
    .quantity-btn {
        width: 30px;
        height: 30px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        border: 1px solid #ddd;
        background-color: white;
        cursor: pointer;
        font-weight: 600;
    }
    
    .quantity-btn:hover {
        background-color: #f5f5f5;
    }
    
    .quantity-value {
        margin: 0 0.5rem;
        font-weight: 600;
    }
    
    /* Checkout styling */
    .checkout-container {
        background-color: white;
        padding: 1.5rem;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    
    .total-section {
        display: flex;
        justify-content: space-between;
        padding: 0.75rem 0;
        border-top: 1px solid #eee;
        font-weight: 600;
    }
    
    .checkout-btn {
        background-color: #2e7d32;
        color: white;
        border: none;
        padding: 0.75rem 1.5rem;
        border-radius: 4px;
        cursor: pointer;
        width: 100%;
        font-weight: 600;
        margin-top: 1rem;
        font-size: 1.1rem;
    }
    
    .checkout-btn:hover {
        background-color: #388e3c;
    }
    
    /* Category filter styling */
    .category-filter {
        display: flex;
        flex-wrap: wrap;
        gap: 0.5rem;
        margin-bottom: 1.5rem;
    }
    
    .category-badge {
        padding: 0.5rem 1rem;
        border-radius: 20px;
        font-size: 0.85rem;
        cursor: pointer;
        transition: background-color 0.2s;
        text-align: center;
    }
    
    .category-badge.active {
        background-color: #1976d2;
        color: white;
        font-weight: 600;
    }
    
    .category-badge:not(.active) {
        background-color: #e0e0e0;
        color: #424242;
    }
    
    .category-badge:hover:not(.active) {
        background-color: #bdbdbd;
    }
    
    /* Search bar styling */
    .search-container {
        display: flex;
        margin-bottom: 1.5rem;
    }
    
    .search-box {
        flex: 1;
        padding: 0.75rem 1rem;
        border: 1px solid #ddd;
        border-radius: 4px;
        font-size: 1rem;
    }
    
    .search-box:focus {
        border-color: #1976d2;
        outline: none;
        box-shadow: 0 0 0 2px rgba(25, 118, 210, 0.2);
    }
    
    /* Utilities */
    .flex-row {
        display: flex;
        flex-direction: row;
    }
    
    .flex-col {
        display: flex;
        flex-direction: column;
    }
    
    .justify-between {
        justify-content: space-between;
    }
    
    .items-center {
        align-items: center;
    }
    
    .text-sm {
        font-size: 0.875rem;
    }
    
    .text-lg {
        font-size: 1.125rem;
    }
    
    .font-bold {
        font-weight: 700;
    }
    
    .text-gray {
        color: #757575;
    }
    
    .mb-1 {
        margin-bottom: 0.25rem;
    }
    
    .mb-2 {
        margin-bottom: 0.5rem;
    }
    
    .mb-4 {
        margin-bottom: 1rem;
    }
    
    .p-2 {
        padding: 0.5rem;
    }
    
    .p-4 {
        padding: 1rem;
    }
    
    /* Empty states */
    .empty-state {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        padding: 3rem;
        background-color: white;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    
    .empty-state-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
        color: #9e9e9e;
    }
    
    .empty-state-text {
        font-size: 1.25rem;
        font-weight: 600;
        margin-bottom: 1rem;
        color: #616161;
    }
</style>
""",
    unsafe_allow_html=True,
)

# Initialize session states
if "cart" not in st.session_state:
    st.session_state.cart = {}

if "wishlist" not in st.session_state:
    st.session_state.wishlist = set()

if "filter_category" not in st.session_state:
    st.session_state.filter_category = "All"

if "search_query" not in st.session_state:
    st.session_state.search_query = ""


# Helper functions
def format_name(name):
    """Format a name to be used as an ID"""
    return name.lower().replace(" ", "_")


def get_discount_percentage(original, current):
    """Calculate discount percentage"""
    if original <= current:
        return 0
    return int(((original - current) / original) * 100)


def filter_products(category="All", search=""):
    """Filter products by category and search query"""
    filtered = products

    # Filter by category if not 'All'
    if category != "All":
        filtered = [p for p in filtered if p["category"] == category]

    # Filter by search query if provided
    if search:
        search = search.lower()
        filtered = [
            p
            for p in filtered
            if search in p["name"].lower() or search in p["description"].lower()
        ]

    return filtered


# Cart functions
def add_to_cart(product_id):
    """Add a product to the cart"""
    if product_id in st.session_state.cart:
        st.session_state.cart[product_id]["quantity"] += 1
    else:
        # Find the product by ID
        product = next((p for p in products if p["id"] == product_id), None)
        if product:
            st.session_state.cart[product_id] = {
                "id": product["id"],
                "name": product["name"],
                "price": product["price"],
                "image": product["thumbnail"],
                "quantity": 1,
            }
    time.sleep(0.1)  # Small delay to ensure UI updates


def remove_from_cart(product_id):
    """Remove a product from the cart"""
    if product_id in st.session_state.cart:
        st.session_state.cart[product_id]["quantity"] -= 1
        if st.session_state.cart[product_id]["quantity"] <= 0:
            del st.session_state.cart[product_id]
    time.sleep(0.1)  # Small delay to ensure UI updates


def update_cart_quantity(product_id, quantity):
    """Update the quantity of a product in the cart"""
    if product_id in st.session_state.cart:
        if quantity <= 0:
            del st.session_state.cart[product_id]
        else:
            st.session_state.cart[product_id]["quantity"] = quantity
    time.sleep(0.1)  # Small delay to ensure UI updates


def clear_cart():
    """Clear the entire cart"""
    st.session_state.cart = {}


def toggle_wishlist(product_id):
    """Add or remove a product from the wishlist"""
    if product_id in st.session_state.wishlist:
        st.session_state.wishlist.remove(product_id)
    else:
        st.session_state.wishlist.add(product_id)


def checkout():
    """Process checkout"""
    # In a real app, this would handle payment processing
    # For this demo, we'll just clear the cart and show a success message
    clear_cart()
    st.session_state.checkout_complete = True
    st.session_state.order_number = f"ORD-{int(time.time())}"
    time.sleep(0.1)  # Small delay to ensure UI updates


# Set filter category
def set_filter_category(category):
    st.session_state.filter_category = category
    time.sleep(0.1)  # Small delay to ensure UI updates


# Set search query
def set_search_query():
    st.session_state.search_query = st.session_state.search_input
    time.sleep(0.1)  # Small delay to ensure UI updates


# Display star rating
def display_stars(rating):
    full_stars = int(rating)
    half_star = rating - full_stars >= 0.5
    empty_stars = 5 - full_stars - (1 if half_star else 0)

    stars = "★" * full_stars
    if half_star:
        stars += "½"
    stars += "☆" * empty_stars

    return stars


# Main application
# Header section
st.markdown(
    '<div class="header-container"><h1 class="site-title">E-Commerce Store</h1></div>',
    unsafe_allow_html=True,
)

# Create tabs for store sections
tabs = st.tabs(["Shop", "Cart", "Wishlist"])

with tabs[0]:  # Shop tab
    # Search bar
    col1, col2 = st.columns([4, 1])
    with col1:
        st.text_input(
            "Search products...", key="search_input", on_change=set_search_query
        )

    # Category filter
    st.markdown('<div class="category-filter">', unsafe_allow_html=True)
    col_all = st.columns(8)
    with col_all[0]:
        if st.button(
            "All",
            key="cat_all",
            help="Show all products",
            use_container_width=True,
            type=(
                "primary" if st.session_state.filter_category == "All" else "secondary"
            ),
        ):
            set_filter_category("All")

    for i, category in enumerate(categories):
        with col_all[(i + 1) % 8]:
            if st.button(
                category,
                key=f"cat_{format_name(category)}",
                help=f"Show only {category} products",
                use_container_width=True,
                type=(
                    "primary"
                    if st.session_state.filter_category == category
                    else "secondary"
                ),
            ):
                set_filter_category(category)
    st.markdown("</div>", unsafe_allow_html=True)

    # Get filtered products
    filtered_products = filter_products(
        st.session_state.filter_category, st.session_state.search_query
    )

    if not filtered_products:
        st.markdown(
            """
        <div class="empty-state">
            <div class="empty-state-icon">🔍</div>
            <div class="empty-state-text">No products found</div>
            <div class="text-gray">Try adjusting your search or filter criteria</div>
        </div>
        """,
            unsafe_allow_html=True,
        )
    else:
        # Display filtered products in a grid
        cols = st.columns(3)
        for i, product in enumerate(filtered_products):
            with cols[i % 3]:
                # Calculate discount percentage if applicable
                discount = get_discount_percentage(
                    product["original_price"], product["price"]
                )

                # Product card with styling
                st.markdown(
                    f"""
                <div class="product-card">
                    <div style="position: relative;">
                        {f'<span class="discount-badge">-{discount}%</span>' if discount > 0 else ''}
                    </div>
                """,
                    unsafe_allow_html=True,
                )

                # Product image
                st.image(product["image"], use_container_width=True)

                # Product details
                st.markdown(
                    f"""
                <h3 class="product-title">{product['name']}</h3>
                
                <div class="rating-container">
                    <span class="rating-stars">{display_stars(product['rating'])}</span>
                    <span class="review-count">({product['reviews']} reviews)</span>
                </div>
                
                <div class="mb-2">
                    <span class="price-tag">${product['price']:.2f}</span>
                    {f'<span class="original-price">${product["original_price"]:.2f}</span>' if discount > 0 else ''}
                </div>
                
                <div class="mb-2">
                    <span class="text-sm text-gray">{product['category']}</span>
                </div>
                
                <div class="mb-2">
                    {product['description'][:100]}{'...' if len(product['description']) > 100 else ''}
                </div>
                
                <div class="mb-2">
                    {''.join([f'<span class="feature-tag">{feature}</span>' for feature in product['features'][:3]])}
                </div>
                """,
                    unsafe_allow_html=True,
                )

                # Buttons
                col1, col2 = st.columns(2)
                with col1:
                    if st.button(
                        "🛒 Add to Cart",
                        key=f"add_{product['id']}",
                        use_container_width=True,
                    ):
                        add_to_cart(product["id"])
                        st.rerun()

                with col2:
                    wishlist_text = (
                        "❤️ Remove"
                        if product["id"] in st.session_state.wishlist
                        else "🤍 Wishlist"
                    )
                    if st.button(
                        wishlist_text,
                        key=f"wish_{product['id']}",
                        use_container_width=True,
                    ):
                        toggle_wishlist(product["id"])
                        st.rerun()

                st.markdown("</div>", unsafe_allow_html=True)

with tabs[1]:  # Cart tab
    st.markdown("<h2>Your Shopping Cart</h2>", unsafe_allow_html=True)

    if not st.session_state.cart:
        st.markdown(
            """
        <div class="empty-state">
            <div class="empty-state-icon">🛒</div>
            <div class="empty-state-text">Your cart is empty</div>
            <div class="text-gray">Add some products to your cart to get started</div>
        </div>
        """,
            unsafe_allow_html=True,
        )
    else:
        # Display cart items with proper styling
        for product_id, item in st.session_state.cart.items():
            st.markdown(
                f"""
            <div class="cart-item">
                <img src="{item['image']}" class="cart-item-image" alt="{item['name']}">
                <div class="cart-item-details">
                    <h3 class="cart-item-title">{item['name']}</h3>
                    <p class="cart-item-price">${item['price']:.2f}</p>
                </div>
            </div>
            """,
                unsafe_allow_html=True,
            )

            # Quantity control with proper buttons
            col1, col2, col3, col4 = st.columns([1, 1, 3, 1])
            with col1:
                if st.button(
                    "➖",
                    key=f"dec_{product_id}",
                    help="Decrease quantity",
                    use_container_width=True,
                ):
                    remove_from_cart(product_id)
                    st.rerun()

            with col2:
                quantity = st.number_input(
                    "Qty",
                    min_value=1,
                    value=item["quantity"],
                    key=f"qty_{product_id}",
                    label_visibility="collapsed",
                )
                if quantity != item["quantity"]:
                    update_cart_quantity(product_id, quantity)
                    st.rerun()

            with col3:
                subtotal = item["price"] * item["quantity"]
                st.markdown(
                    f"<p class='text-lg font-bold'>Subtotal: ${subtotal:.2f}</p>",
                    unsafe_allow_html=True,
                )

            with col4:
                if st.button(
                    "➕",
                    key=f"inc_{product_id}",
                    help="Increase quantity",
                    use_container_width=True,
                ):
                    add_to_cart(product_id)
                    st.rerun()

        # Calculate cart totals
        subtotal = sum(
            item["price"] * item["quantity"] for item in st.session_state.cart.values()
        )
        shipping = 0 if subtotal > 100 else 10
        tax = subtotal * 0.08  # 8% tax
        total = subtotal + shipping + tax

        # Checkout section
        st.markdown('<div class="checkout-container">', unsafe_allow_html=True)
        st.markdown("<h3>Order Summary</h3>", unsafe_allow_html=True)

        st.markdown(
            f"""
        <div class="total-section">
            <span>Subtotal</span>
            <span>${subtotal:.2f}</span>
        </div>
        <div class="total-section">
            <span>Shipping {"(Free over $100)" if shipping == 0 else ""}</span>
            <span>${shipping:.2f}</span>
        </div>
        <div class="total-section">
            <span>Tax (8%)</span>
            <span>${tax:.2f}</span>
        </div>
        <div class="total-section" style="font-size: 1.25rem;">
            <span>Total</span>
            <span>${total:.2f}</span>
        </div>
        """,
            unsafe_allow_html=True,
        )

        # Checkout button
        if st.button("Proceed to Checkout", type="primary", use_container_width=True):
            checkout()
            st.rerun()

        # Clear cart button
        if st.button("Clear Cart", type="secondary", use_container_width=True):
            clear_cart()
            st.rerun()

        st.markdown("</div>", unsafe_allow_html=True)

with tabs[2]:  # Wishlist tab
    st.markdown("<h2>Your Wishlist</h2>", unsafe_allow_html=True)

    if not st.session_state.wishlist:
        st.markdown(
            """
        <div class="empty-state">
            <div class="empty-state-icon">🤍</div>
            <div class="empty-state-text">Your wishlist is empty</div>
            <div class="text-gray">Add products to your wishlist to save them for later</div>
        </div>
        """,
            unsafe_allow_html=True,
        )
    else:
        # Get wishlist products
        wishlist_products = [
            p for p in products if p["id"] in st.session_state.wishlist
        ]

        # Display wishlist items in a grid
        cols = st.columns(3)
        for i, product in enumerate(wishlist_products):
            with cols[i % 3]:
                # Calculate discount percentage if applicable
                discount = get_discount_percentage(
                    product["original_price"], product["price"]
                )

                # Product card with styling
                st.markdown(
                    f"""
                <div class="product-card">
                    <div style="position: relative;">
                        {f'<span class="discount-badge">-{discount}%</span>' if discount > 0 else ''}
                    </div>
                """,
                    unsafe_allow_html=True,
                )

                # Product image
                st.image(product["image"], use_container_width=True)

                # Product details
                st.markdown(
                    f"""
                <h3 class="product-title">{product['name']}</h3>
                
                <div class="rating-container">
                    <span class="rating-stars">{display_stars(product['rating'])}</span>
                    <span class="review-count">({product['reviews']} reviews)</span>
                </div>
                
                <div class="mb-2">
                    <span class="price-tag">${product['price']:.2f}</span>
                    {f'<span class="original-price">${product["original_price"]:.2f}</span>' if discount > 0 else ''}
                </div>
                
                <div class="mb-2">
                    <span class="text-sm text-gray">{product['category']}</span>
                </div>
                """,
                    unsafe_allow_html=True,
                )

                # Buttons
                col1, col2 = st.columns(2)
                with col1:
                    if st.button(
                        "🛒 Add to Cart",
                        key=f"wish_add_{product['id']}",
                        use_container_width=True,
                    ):
                        add_to_cart(product["id"])
                        st.rerun()

                with col2:
                    if st.button(
                        "❌ Remove",
                        key=f"wish_remove_{product['id']}",
                        use_container_width=True,
                    ):
                        toggle_wishlist(product["id"])
                        st.rerun()

                st.markdown("</div>", unsafe_allow_html=True)

# Display checkout success message
if st.session_state.get("checkout_complete", False):
    order_number = st.session_state.get("order_number", "unknown")

    st.success(f"Your order #{order_number} has been placed successfully!")
    st.balloons()

    st.markdown(
        """
    <div style="background-color: white; padding: 2rem; border-radius: 8px; text-align: center; margin-top: 1rem;">
        <h2>Thank You For Your Order!</h2>
        <p style="font-size: 1.1rem; margin: 1rem 0;">Your order has been confirmed and will be shipped soon.</p>
        <div style="font-size: 5rem; margin: 2rem 0;">🎉</div>
    </div>
    """,
        unsafe_allow_html=True,
    )

    # Reset checkout state after displaying the message
    st.session_state.checkout_complete = False
