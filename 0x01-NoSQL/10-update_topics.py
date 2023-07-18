#!/usr/bin/env python3
"""
updating documents
"""


def update_topics(mongo_collection, name, topics):
    """
    Updates topics
    """
    mongo_collection.update_many({'name': name},
                                 {'$set': {'topics': topics}})
