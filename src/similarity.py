def calculate_similarity_score(
        user,
        product,
        products
):
    """
    Calculate recommendation score
    """

    score = 0
    explanation = []

    # Purchase history match
    for purchased_id in user.purchase_history:

        if purchased_id in products:

            purchased_product = products[
                purchased_id
            ]

            # Same category
            if (
                purchased_product.category
                == product.category
            ):
                score += 5
                explanation.append(
                    "Same category"
                )

            # Same brand
            if (
                purchased_product.brand
                == product.brand
            ):
                score += 3
                explanation.append(
                    "Same brand"
                )

    # Search history match
    for keyword in user.search_history:

        keyword = keyword.lower()

        if (
            keyword
            in product.name.lower()
        ):
            score += 4
            explanation.append(
                "Search match"
            )

        if (
            keyword
            in product.category.lower()
        ):
            score += 3

    # Cart similarity
    for cart_id in user.cart_items:

        if cart_id in products:

            cart_product = products[
                cart_id
            ]

            if (
                cart_product.category
                == product.category
            ):
                score += 3
                explanation.append(
                    "Cart similarity"
                )

    # Rating boost
    score += product.rating

    return score, explanation


def get_similar_products(
        product_id,
        products,
        top_n=5
):
    """
    Get similar products
    """

    if product_id not in products:
        return []

    target_product = products[
        product_id
    ]

    similar_products = []

    for pid, product in products.items():

        if pid == product_id:
            continue

        similarity_score = 0

        # Same category
        if (
            product.category
            == target_product.category
        ):
            similarity_score += 5

        # Same brand
        if (
            product.brand
            == target_product.brand
        ):
            similarity_score += 3

        # Rating similarity
        rating_gap = abs(
            product.rating
            - target_product.rating
        )

        similarity_score += (
            5 - rating_gap
        )

        similar_products.append(
            (
                similarity_score,
                product
            )
        )

    similar_products.sort(
        reverse=True,
        key=lambda x: x[0]
    )

    return similar_products[:top_n]