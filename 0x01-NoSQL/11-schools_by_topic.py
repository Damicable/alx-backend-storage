#!/usr/bin/env python3
"""Python function module to find documents"""


def schools_by_topic(mongo_collection, topic):
    """
    schools_by_topic - Find mongo collection by topics
    @mongo_collection: Mongo collection object
    @topic: Topic to filter by
    Return: List of documents
    """
    return mongo_collection.find({'topics': {'$elemMatch': {'$eq': topic}}})
