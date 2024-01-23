#!/usr/bin/env python3
"""Python function module"""


def update_topics(mongo_collection, name, topics):
    """
    update_topics - Update mongo collection topics
    @mongo_collection: Mongo collection object
    @name: Name of school to update
    @topics: List of topics to add
    Return: Nothing
    """
    mongo_collection.update_one({'name': name}, {'$set': {'topics': topics}})
