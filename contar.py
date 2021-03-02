def app(environ, start_response):
    """Simplest possible application object"""
    status = '200 OK'
    data = b'<h1>Pagina Teste , Status resposta= </h1>\n',status
    headers = [('Content-type', 'text/html')]
    start_response(status, headers)
    return [data]

def somar(x,y):
    return (x+y)