def app(environ, start_response):
    """Simplest possible application object"""
    status = "200 ok"
    data = b'<h1>Pagina Teste , Status resposta= </h1>\n',b'200 OK'
    headers = [('Content-type', 'text/html')]
    start_response(status, headers)
    return [data]

def somar(x,y):
    return (x+y)