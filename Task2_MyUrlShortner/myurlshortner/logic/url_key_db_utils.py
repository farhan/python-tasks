from myurlshortner.models import UrlKey

# Maximum no of rows retrieved at one time
DATA_SLICE_SIZE = 1000


def get_best_key(url):
    no_of_records = UrlKey.objects.count()
    offset = 0
    while offset < no_of_records:
        rows_slice = get_slice_of_rows(offset, DATA_SLICE_SIZE)
        for urlKey in rows_slice:
            # If no key found that is a part of url
            if urlKey.is_assigned:
                first_non_assigned_key = get_first_non_assigned_key();
                if first_non_assigned_key is not None:
                    return first_non_assigned_key
                else:
                    # All keys has been assigned to urls
                    return get_oldest_assigned_key()
            # If found a key that is a part of url
            if urlKey.key_name in url and not urlKey.is_assigned:
                return urlKey
        offset += DATA_SLICE_SIZE


def get_first_non_assigned_key():
    key = UrlKey.objects.first()
    return key if not key.is_assigned else None


def get_oldest_assigned_key():
    return UrlKey.objects.order_by('assigned_timestamp').first()


def get_slice_of_rows(offset, no_of_rows):
    return UrlKey.objects.all().only('key_name', 'is_assigned')[offset:(offset + no_of_rows)]
