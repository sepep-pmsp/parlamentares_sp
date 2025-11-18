import urllib.parse


def url_encode(input_string):

    encoded = urllib.parse.quote_plus(input_string)
    return encoded
