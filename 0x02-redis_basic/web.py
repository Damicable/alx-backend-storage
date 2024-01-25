#!/usr/bin/env python3
"""Web implementation function module"""


def get_page(url: str) -> str:
    """
    get_page - Function  to obtain the HTML content of a particular URL.
    @url: The url to obtain HTML content from
    Return: String
    """
    redis_instance = redis.Redis()
    contents = requests.get(url).text
    r.setex(url, 10, contents)
    r.incr('count' + ':' + url)
