class User:
    """
    User class to store user interactions
    """

    def __init__(self, user_id, name):
        self.user_id = int(user_id)
        self.name = name

        # User activity
        self.purchase_history = []
        self.search_history = []
        self.cart_items = []
        self.ratings = {}

    def add_purchase(self, product_id):
        self.purchase_history.append(product_id)

    def add_search(self, keyword):
        self.search_history.append(keyword)

    def add_to_cart(self, product_id):
        self.cart_items.append(product_id)

    def add_rating(self, product_id, rating):
        self.ratings[product_id] = rating

    def display_user(self):
        print("\nUser Information")
        print("-" * 40)
        print(f"User ID : {self.user_id}")
        print(f"Name    : {self.name}")
        print(f"Purchases : {self.purchase_history}")
        print(f"Searches : {self.search_history}")
        print(f"Cart     : {self.cart_items}")
        print(f"Ratings  : {self.ratings}")

    def __str__(self):
        return f"{self.user_id} - {self.name}"