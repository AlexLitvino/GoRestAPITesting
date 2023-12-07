from urllib.parse import urljoin, quote_plus


def url_join(*parts):
    """
    Combines several parts of url into one
    Taken with gratitude at @techouse (https://stackoverflow.com/a/55722792/3364446)
    """
    return urljoin(parts[0], "/".join(quote_plus(part.strip("/"), safe="/") for part in parts[1:]))
