#!/usr/bin/env python3
"""
Function to update the topics for a school document based on the name.
"""

def update_topics(mongo_collection, name, topics):
    """
    Updates the 'topics' field of the school document with the specified 'name'.
    Args:
        mongo_collection: The pymongo collection object.
        name (str): The name of the school to update.
        topics (list of str): The list of topics to set for the school.
    """
    mongo_collection.update_one(
        { 'name': name },
        { '$set': { 'topics': topics } }
    )
