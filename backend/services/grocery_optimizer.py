def generate_grocery_list(preferences, dietary_restrictions):
    # Simple example of grocery list optimization
    base_list = ['milk', 'bread', 'eggs', 'tomatoes', 'chicken']

    # Filter out items based on dietary restrictions
    if 'vegetarian' in dietary_restrictions:
        base_list.remove('chicken')

    # Add user preferences
    if 'cheese' in preferences:
        base_list.append('cheese')

    return base_list


import numpy as np
from collections import Counter
from sklearn.metrics.pairwise import cosine_similarity

def generate_grocery_list(preferences, dietary_restrictions, past_purchases):
    base_list = ['milk', 'bread', 'eggs', 'tomatoes', 'chicken']

    # Example of item co-occurrence (usually stored in the database)
    purchase_history = [
        ['milk', 'bread', 'eggs'],
        ['eggs', 'chicken', 'bread'],
        ['milk', 'cheese', 'bread'],
        ['tomatoes', 'eggs'],
        ['cheese', 'bread', 'chicken'],
    ]

    # Count occurrences of items
    item_counter = Counter(item for sublist in purchase_history for item in sublist)

    # Create item-to-item similarity matrix using cosine similarity
    unique_items = list(item_counter.keys())
    item_vectors = np.array([[1 if item in purchases else 0 for item in unique_items] for purchases in purchase_history])
    similarity_matrix = cosine_similarity(item_vectors)

    # Generate item recommendations based on similarity
    recommended_items = recommend_items(unique_items, similarity_matrix, past_purchases)

    # Add preferences and remove items restricted by dietary constraints
    final_list = base_list + recommended_items
    if 'vegetarian' in dietary_restrictions:
        final_list = [item for item in final_list if item != 'chicken']

    return final_list

def recommend_items(unique_items, similarity_matrix, past_purchases):
    if not past_purchases:
        return []

    purchase_indices = [unique_items.index(item) for item in past_purchases if item in unique_items]
    if not purchase_indices:
        return []

    # Find similar items
    similar_items_scores = similarity_matrix[purchase_indices].mean(axis=0)
    top_similar_indices = np.argsort(-similar_items_scores)[:5]  # Top 5 similar items
    recommended_items = [unique_items[i] for i in top_similar_indices if unique_items[i] not in past_purchases]

    return recommended_items
