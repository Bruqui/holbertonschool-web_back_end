#!/usr/bin/env python3
"""
Function to insert a new school document in the MongoDB collection using
kwargs.
"""

def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document into the MongoDB collection with attributes passed
    as kwargs.
    Args:
        mongo_collection: The pymongo collection object.
        **kwargs: The fields to insert in the document.
    Returns:
        The _id of the newly inserted document.
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
