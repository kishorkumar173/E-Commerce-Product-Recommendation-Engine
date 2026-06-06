def generate_report(
        user_id,
        recommendations,
        file_path="outputs/recommendation_report.txt"
):
    """
    Generate recommendation report
    """

    with open(
            file_path,
            "w",
            encoding="utf-8"
    ) as file:

        file.write(
            "=" * 60
        )

        file.write("\n")

        file.write(
            "E-COMMERCE PRODUCT "
            "RECOMMENDATION REPORT\n"
        )

        file.write(
            "=" * 60
        )

        file.write("\n\n")

        file.write(
            f"User ID: "
            f"{user_id}\n"
        )

        file.write(
            "-" * 60
        )

        file.write("\n")

        for (
                score,
                product,
                explanation
        ) in recommendations:

            file.write(
                f"\nScore: "
                f"{score:.2f}\n"
            )

            file.write(
                f"Product ID: "
                f"{product.product_id}\n"
            )

            file.write(
                f"Name: "
                f"{product.name}\n"
            )

            file.write(
                f"Category: "
                f"{product.category}\n"
            )

            file.write(
                f"Brand: "
                f"{product.brand}\n"
            )

            file.write(
                f"Price: ₹"
                f"{product.price}\n"
            )

            file.write(
                f"Rating: "
                f"{product.rating}\n"
            )

            file.write(
                "Why Recommended: "
            )

            if explanation:

                file.write(
                    ", ".join(
                        explanation
                    )
                )

            else:

                file.write(
                    "Trending Product"
                )

            file.write("\n")

            file.write(
                "-" * 60
            )

            file.write("\n")

    print(
        "\nRecommendation "
        "report saved "
        "successfully!"
    )