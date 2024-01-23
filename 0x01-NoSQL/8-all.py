#!/usr/bin/env python3
""" Python function module"""


def list_all(mongo_collection):
    """
    list_all - function that lists all document in a collection
    @mongo_collection: Mongo collection object
    Return: list of documents otherwise, empty list
    """
    if mongo_collection.count_documents({}) == 0:
        return []
    return mongo_collection.find()
