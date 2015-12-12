

def convert_headers_to_environ(headers):
    """
    Converts HTTP headers into WSGI environ variables.
    """
    return {
        'HTTP_' + key.replace('-', '_').upper(): value.strip()
        for key, value in headers.items()
    }
