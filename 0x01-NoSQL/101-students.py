#!/usr/bin/env python3
"""
average
"""
from collections import OrderedDict


def top_students(mongo_collection):
    """
    Gets list 
    """
    pipeline = [{'$addFields': {'averageScore': {'$avg': '$topics.score'}}},
                {'$sort': OrderedDict([('averageScore', -1), ('name', 1)])}]
    return mongo_collection.aggregate(pipeline)
