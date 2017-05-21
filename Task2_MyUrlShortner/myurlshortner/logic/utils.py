import re


def clean_key(url_key):
    url_key = url_key.lower()
    return re.sub('[^a-z0-9]', '', url_key)
