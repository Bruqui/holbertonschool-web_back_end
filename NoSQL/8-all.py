#!/usr/bin/env python3
"""
Function to list all documents in a MongoDB collection.
"""


def list_all(mongo_collection):
    """
    Lists all documents in the provided MongoDB collection.
    Args:
        mongo_collection: The pymongo collection object.
    Returns:
        A list of all documents in the collection or an empty list if no
        documents.
    """
    return list(mongo_collection.find())
