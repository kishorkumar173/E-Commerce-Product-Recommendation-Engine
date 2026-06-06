import csv

from src.product import Product
from src.user import User


def load_products(file_path="data/products.csv"):
    """
    Load products from CSV
    """

    products = {}

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                product = Product(
                    row["product_id"],
                    row["name"],
                    row["category"],
                    row["brand"],
                    row["price"],
                    row["rating"]
                )

                # Store in HashMap
                products[product.product_id] = product

    except FileNotFoundError:
        print("Products CSV file not found.")

    return products


def load_users(file_path="data/users.csv"):
    """
    Load users from CSV
    """

    users = {}

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:

                user = User(
                    row["user_id"],
                    row["name"]
                )

                # Purchases
                purchases = row["purchases"].split(",")

                for item in purchases:
                    if item.strip():
                        user.add_purchase(int(item.strip()))

                # Search History
                searches = row["search_history"].split(",")

                for search in searches:
                    if search.strip():
                        user.add_search(search.strip())

                # Cart Items
                cart_items = row["cart_items"].split(",")

                for item in cart_items:
                    if item.strip():
                        user.add_to_cart(int(item.strip()))

                users[user.user_id] = user

    except FileNotFoundError:
        print("Users CSV file not found.")

    return users