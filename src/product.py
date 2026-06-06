class Product:
    """
    Product class to store product details
    """

    def __init__(
        self,
        product_id,
        name,
        category,
        brand,
        price,
        rating
    ):
        self.product_id = int(product_id)
        self.name = name
        self.category = category
        self.brand = brand
        self.price = float(price)
        self.rating = float(rating)

    def display_product(self):
        """
        Display product details
        """
        print("\nProduct Details")
        print("-" * 40)
        print(f"ID       : {self.product_id}")
        print(f"Name     : {self.name}")
        print(f"Category : {self.category}")
        print(f"Brand    : {self.brand}")
        print(f"Price    : ₹{self.price}")
        print(f"Rating   : {self.rating}")

    def __str__(self):
        return (
            f"{self.product_id} | "
            f"{self.name} | "
            f"{self.category} | "
            f"{self.brand} | "
            f"₹{self.price} | "
            f"⭐ {self.rating}"
        )