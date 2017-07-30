#!/usr/bin/env python
from myurlshortner.wsgi import *
from myurlshortner.models import UrlKey
from myurlshortner.logic import utils


def clean_and_populate():
    # Read data from file
    file = open('datapopulator/words.txt')
    try:
        for word in file:
            # Clean data
            key = utils.clean_key(word)
            # Insert data into database
            print(key)
            insert_key_into_db(key)
    finally:
        file.close()


def insert_key_into_db(url_key):
    key = UrlKey(key_name=url_key)
    if UrlKey.objects.filter(key_name=url_key).count() == 0:
        key.save()


def main():
    clean_and_populate()


if __name__ == "__main__": main()
