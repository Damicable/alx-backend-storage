#!/usr/bin/env python3
"""Python function module """


def top_students(mongo_collection):
    """
    top_students - This returns all students sorted by average score
    @mongo_collection: pymongo collection object.
    Return: Average score
    """
    if mongo_collection.count_documents({}) == 0:
        return []

    return mongo_collection.aggregate([
            {
                '$project': {
                    'name': '$name',
                    'averageScore': {'$avg': '$topics.score'}
                }
            },
            {'$sort': {'averageScore': -1}}
        ])
