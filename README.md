# DSA Project | E-Commerce Product Recommendation Engine

## Project Overview

The **E-Commerce Product Recommendation Engine** is an industry-oriented recommendation system developed using **Python** and **Data Structures & Algorithms (DSA)** concepts.

This project simulates how modern e-commerce platforms recommend products to users based on:

* Purchase history
* Search history
* Cart activity
* Product similarity
* Product ratings
* Category preference

The system generates **personalized product recommendations**, identifies **similar products**, supports **search functionality**, and recommends **trending products** using recommendation scoring and ranking algorithms.

This project demonstrates practical applications of **HashMaps, Sorting, Priority Queue logic, Lists, Searching, and Recommendation Algorithms** in a real-world e-commerce scenario.

---

## Problem Statement

In online shopping platforms, users often struggle to find relevant products due to the huge number of available items.

Traditional search methods may not always show the most useful products.

The objective of this project is to build an intelligent recommendation engine that improves product discovery by analyzing:

* User purchase history
* Search behavior
* Cart items
* Product category similarity
* Product ratings

The system provides personalized product recommendations to improve shopping experience and product relevance.

---

## Industry Relevance

Modern e-commerce platforms such as Amazon, Flipkart, Myntra, and Netflix-style systems heavily depend on recommendation engines.

Recommendation systems are used for:

### Personalized Recommendations

Suggest products based on user behavior.

### Similar Product Suggestions

Recommend products similar to viewed products.

### Trending Products

Display top-performing or highly rated products.

### Category-Based Suggestions

Show best products within a category.

### Cold Start Handling

Recommend products to new users who have no activity history.

This project simulates these real-world recommendation mechanisms.

---

## Features

### Personalized Product Recommendation

Recommends products using:

* Purchase history
* Search history
* Cart items
* Product similarity
* Ratings

### Similar Products Recommendation

Finds products similar to a selected product using:

* Category similarity
* Brand similarity
* Rating similarity

### Product Search

Search products by:

* Product Name
* Category
* Brand

### Category-Based Recommendation

Displays top-rated products for a selected category.

### Trending Products

Shows top trending products based on product ratings.

### Recommendation Explanation

Explains why a product was recommended.

Example:

```text
✓ Same category
✓ Same brand
✓ Search match
✓ Cart similarity
```

### Recommendation Report Generation

Automatically generates recommendation reports in:

```text
outputs/recommendation_report.txt
```

---

## Workflow

```text
User Activity
     ↓
Purchase History
Search History
Cart Items
     ↓
Recommendation Engine
     ↓
Similarity Calculation
     ↓
Recommendation Scoring
     ↓
Sorting & Ranking
     ↓
Top Recommended Products
```

---

## DSA Concepts Used

| DSA Concept            | Usage                                       |
| ---------------------- | ------------------------------------------- |
| HashMap (Dictionary)   | Fast product and user lookup                |
| Lists                  | Store purchase, cart and search history     |
| Sorting                | Rank products based on recommendation score |
| Searching              | Product search functionality                |
| Priority Queue Logic   | Top-N recommendation ranking                |
| Recommendation Scoring | Personalized recommendation system          |

---

## Technologies Used

### Programming Language

* Python

### Libraries

Built-in Python libraries:

* csv
* heapq

No external dependencies are required.

---

## Project Architecture

```text
E-Commerce-Product-Recommendation-Engine/
│
├── data/
│   ├── products.csv
│   └── users.csv
│
├── src/
│   ├── __init__.py
│   ├── product.py
│   ├── user.py
│   ├── dataset.py
│   ├── similarity.py
│   ├── recommender.py
│   ├── ranking.py
│   └── report.py
│
├── outputs/
│   └── recommendation_report.txt
│
├── images/
│
├── docs/
│
├── README.md
├── requirements.txt
├── .gitignore
└── main.py
```

---

## Dataset Information

### Product Dataset

Contains:

* Product ID
* Product Name
* Category
* Brand
* Price
* Rating

Example:

| Product ID | Name               | Category    |
| ---------- | ------------------ | ----------- |
| 101        | Nike Running Shoes | Footwear    |
| 104        | Apple iPhone 15    | Electronics |

---

### User Dataset

Contains:

* User ID
* Purchase History
* Search History
* Cart Items

Example:

```text
User 1:
Purchases → Shoes, Headphones
Searches → Running Shoes
Cart → Watch
```

---

## Installation Guide

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/E-Commerce-Product-Recommendation-Engine.git
```

### Navigate to Project

```bash
cd E-Commerce-Product-Recommendation-Engine
```

### Run Project

```bash
python main.py
```

---

## Menu Options

```text
1. View Products
2. View Users
3. Get Recommendations
4. Similar Products
5. Search Product
6. Category Recommendations
7. Trending Products
8. Exit
```

---

## Sample Output

### Personalized Recommendation

```text
Top 5 Recommendations for User 1

Score: 13.50
Nike Smart Watch

Why Recommended:
✓ Same category
✓ Search match
✓ Cart similarity
```

---

### Similar Products

```text
Nike Running Shoes

Recommended Similar Products:
- Adidas Sneakers
- Puma Sports Shoes
- Campus Running Shoes
```

---

## Screenshots

### Project Structure

Add screenshot here

### Main Menu

Add screenshot here

### Recommendation Output

Add screenshot here

### Similar Products

Add screenshot here

### Search Product

Add screenshot here

### Recommendation Report

Add screenshot here

---

## Future Improvements

Future enhancements include:

* Machine Learning recommendation model
* Collaborative filtering
* Cosine similarity
* Database integration
* Web application interface
* Real-time recommendation API

---

## Learning Outcomes

By building this project, I learned:

* Data Structures and Algorithms
* HashMap implementation
* Sorting and Ranking Logic
* Recommendation System Design
* CSV Data Handling
* Object-Oriented Programming
* Backend System Design
* GitHub Project Structuring

---

## Conclusion

The **E-Commerce Product Recommendation Engine** demonstrates how DSA concepts can be applied to build intelligent recommendation systems for modern e-commerce applications.

This project successfully combines:

* Real-world recommendation logic
* Data Structures & Algorithms
* Backend development principles
* Personalized recommendation techniques

to create a scalable and practical recommendation engine.

---

## Author

**Kishor Kumar L**

Computer Science Engineering (AIML)

GitHub: Add your GitHub profile link here
