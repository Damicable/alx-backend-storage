#!/usr/bin/env python3
""" Insert function module """


def insert_school(mongo_collection, **kwargs):
    """
    insert_school - Functio to insert new document
    @mongo_collection: pymongo collection object
    @kwargs: Argument
    Return: New _id
    """
    mongo_creation = mongo_collection.insert_one(kwargs)
    return mongo_creation.inserted_id
