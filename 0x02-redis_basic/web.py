#!/usr/bin/env python3
"""
Web cache implementation
"""
import requests
import redis
from functools import wraps

store = redis.Redis()


def count_url_access(method):
    """
    count_url_access - A decorator counting how many times
    a Url is accessed
    @method: Method to count 
    """
    @wraps(method)
    def wrapper(url):
        cached_key = "cached:" + url
        cached_data = store.get(cached_key)
        if cached_data:
            return cached_data.decode("utf-8")

        count_key = "count:" + url
        html = method(url)

        store.incr(count_key)
        store.set(cached_key, html)
        store.expire(cached_key, 10)
        return html
    return wrapper


@count_url_access
def get_page(url: str) -> str:
    """
    get_page - Fetch pages from a url
    @url: Url to fetch from
    Returns: String
    """
    res = requests.get(url)
    return res.text
