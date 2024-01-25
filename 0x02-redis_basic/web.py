#!/usr/bin/env python3
"""Web function cche implemention module"""


import requests
import redis


def get_page(url: str) -> str:
    """
    get_page - Function to fetch pages from a url
    @url: Url to fetch pages from
    Returns: String
    """
    redis_instance = redis.Redis()
    contents = requests.get(url).text
    r.setex(url, 10, contents)
    r.incr('count' + ':' + url)
