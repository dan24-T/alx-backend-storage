#!/usr/bin/env python3
"""
finding documents
"""

def list_all(mongo_collection):
    """
    Lists  all documents
    """
    return mongo_collection.find()
