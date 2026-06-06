from src.similarity import (
    calculate_similarity_score,
    get_similar_products
)


class RecommendationEngine:

    def __init__(
            self,
            products,
            users
    ):
        self.products = products
        self.users = users

    def recommend_products(
            self,
            user_id,
            top_n=5
    ):
        """
        Personalized recommendation
        """

        if user_id not in self.users:
            return []

        user = self.users[user_id]

        scored_products = []

        # Cold start logic
        if len(user.purchase_history) == 0:

            for product in (
                    self.products.values()
            ):

                scored_products.append(
                    (
                        product.rating,
                        product,
                        ["Trending Product"]
                    )
                )

            scored_products.sort(
                reverse=True,
                key=lambda x: x[0]
            )

            return scored_products[:top_n]

        # Personalized recommendation
        for (
                product_id,
                product
        ) in self.products.items():

            # Skip purchased items
            if (
                    product_id
                    in user.purchase_history
            ):
                continue

            score, explanation = (
                calculate_similarity_score(
                    user,
                    product,
                    self.products
                )
            )

            scored_products.append(
                (
                    score,
                    product,
                    explanation
                )
            )

        scored_products.sort(
            reverse=True,
            key=lambda x: x[0]
        )

        return scored_products[:top_n]

    def similar_products(
            self,
            product_id,
            top_n=5
    ):
        """
        Similar products
        """

        return get_similar_products(
            product_id,
            self.products,
            top_n
        )

    def search_products(
            self,
            keyword
    ):
        """
        Search products
        """

        keyword = keyword.lower()

        results = []

        for product in (
                self.products.values()
        ):

            if (
                    keyword
                    in product.name.lower()
                    or
                    keyword
                    in product.category.lower()
                    or
                    keyword
                    in product.brand.lower()
            ):

                results.append(
                    product
                )

        return results

    def category_recommendations(
            self,
            category,
            top_n=5
    ):
        """
        Category recommendations
        """

        category_products = []

        for product in (
                self.products.values()
        ):

            if (
                    product.category.lower()
                    == category.lower()
            ):

                category_products.append(
                    product
                )

        category_products.sort(
            reverse=True,
            key=lambda x: x.rating
        )

        return category_products[:top_n]

    def trending_products(
            self,
            top_n=5
    ):
        """
        Trending products
        """

        products = list(
            self.products.values()
        )

        products.sort(
            reverse=True,
            key=lambda x: x.rating
        )

        return products[:top_n]