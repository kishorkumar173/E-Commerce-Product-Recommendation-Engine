from src.dataset import (
    load_products,
    load_users
)

from src.recommender import (
    RecommendationEngine
)

from src.report import (
    generate_report
)


def display_products(products):
    """
    Display all products
    """

    print("\nAvailable Products")
    print("-" * 70)

    for product in products.values():
        print(product)


def display_users(users):
    """
    Display all users
    """

    print("\nAvailable Users")
    print("-" * 70)

    for user in users.values():
        print(user)


def recommendation_menu(
        engine,
        users
):
    """
    Personalized recommendation
    """

    try:
        user_id = int(
            input(
                "\nEnter User ID: "
            )
        )

        if user_id not in users:
            print("Invalid User ID.")
            return

        top_n = int(
            input(
                "Enter Top N recommendations: "
            )
        )

        recommendations = (
            engine.recommend_products(
                user_id,
                top_n
            )
        )

        print(
            f"\nTop {top_n} "
            f"Recommendations "
            f"for User {user_id}"
        )

        print("-" * 70)

        for (
                score,
                product,
                explanation
        ) in recommendations:

            print(
                f"Score: "
                f"{score:.2f}"
            )

            print(product)

            print(
                "Why Recommended:"
            )

            if explanation:
                for reason in explanation:
                    print(
                        f"✓ {reason}"
                    )
            else:
                print(
                    "✓ Trending Product"
                )

            print("-" * 40)

        generate_report(
            user_id,
            recommendations
        )

    except ValueError:
        print(
            "Please enter "
            "valid numbers."
        )


def similar_products_menu(
        engine
):
    """
    Similar products
    """

    try:
        product_id = int(
            input(
                "\nEnter Product ID: "
            )
        )

        top_n = int(
            input(
                "Enter number of "
                "similar products: "
            )
        )

        similar_products = (
            engine.similar_products(
                product_id,
                top_n
            )
        )

        print(
            "\nSimilar Products"
        )

        print("-" * 70)

        for (
                score,
                product
        ) in similar_products:

            print(
                f"Similarity Score: "
                f"{score:.2f}"
            )

            print(product)

            print("-" * 40)

    except ValueError:
        print(
            "Invalid input."
        )


def search_products_menu(
        engine
):
    """
    Search products
    """

    keyword = input(
        "\nEnter product "
        "name/category/brand: "
    )

    results = (
        engine.search_products(
            keyword
        )
    )

    print("\nSearch Results")
    print("-" * 70)

    if not results:
        print(
            "No products found."
        )
        return

    for product in results:
        print(product)


def category_menu(
        engine
):
    """
    Category recommendations
    """

    category = input(
        "\nEnter Category: "
    )

    top_n = int(
        input(
            "Top N products: "
        )
    )

    products = (
        engine.category_recommendations(
            category,
            top_n
        )
    )

    print(
        f"\nTop Products "
        f"in {category}"
    )

    print("-" * 70)

    for product in products:
        print(product)


def trending_menu(
        engine
):
    """
    Trending products
    """

    top_n = int(
        input(
            "\nTop N trending "
            "products: "
        )
    )

    products = (
        engine.trending_products(
            top_n
        )
    )

    print(
        "\nTrending Products"
    )

    print("-" * 70)

    for product in products:
        print(product)


def main():

    print(
        "\nLoading datasets..."
    )

    print("-" * 70)

    products = (
        load_products()
    )

    users = (
        load_users()
    )

    engine = (
        RecommendationEngine(
            products,
            users
        )
    )

    while True:

        print("\n")
        print("=" * 70)

        print(
            "E-Commerce Product "
            "Recommendation Engine"
        )

        print("=" * 70)

        print(
            "1. View Products"
        )

        print(
            "2. View Users"
        )

        print(
            "3. Get "
            "Recommendations"
        )

        print(
            "4. Similar Products"
        )

        print(
            "5. Search Product"
        )

        print(
            "6. Category "
            "Recommendations"
        )

        print(
            "7. Trending "
            "Products"
        )

        print(
            "8. Exit"
        )

        choice = input(
            "\nEnter choice: "
        )

        if choice == "1":
            display_products(
                products
            )

        elif choice == "2":
            display_users(
                users
            )

        elif choice == "3":
            recommendation_menu(
                engine,
                users
            )

        elif choice == "4":
            similar_products_menu(
                engine
            )

        elif choice == "5":
            search_products_menu(
                engine
            )

        elif choice == "6":
            category_menu(
                engine
            )

        elif choice == "7":
            trending_menu(
                engine
            )

        elif choice == "8":

            print(
                "\nThank you "
                "for using system!"
            )

            break

        else:
            print(
                "Invalid choice."
            )


if __name__ == "__main__":
    main()