import heapq


def get_top_recommendations(
        scored_products,
        top_n=5
):
    """
    Return top N products
    using heap
    """

    top_products = heapq.nlargest(
        top_n,
        scored_products,
        key=lambda x: x[0]
    )

    return top_products