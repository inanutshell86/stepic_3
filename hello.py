def app (environ, start_response):
    status = '200 OK'
    headers = [('Content-type', 'text/plain')]
    body = ''
    for line in environ['QUERY_STRING'].split('&'):
        body = body + line + '\n'
    start_response(status, headers)
    return [body]
