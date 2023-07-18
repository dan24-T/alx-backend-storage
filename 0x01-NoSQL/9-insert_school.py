#!/usr/bin/env python3
"""
 inserting new documents
"""

def insert_school(mongo_collection, **kwargs):
    """ Inserts a new document
    """
    return mongo_collection.insert_one(kwargs).inserted_id
