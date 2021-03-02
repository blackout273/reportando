def app(environ, start_response):
    """Simplest possible application object"""
    status = '200 OK'
    data = b'<h1>Pagina Teste , Status resposta= {status}</h1>\n'.__format__(status)
    headers = [('Content-type', 'text/html')]
    start_response(status, headers)
    return [data]

def somar(x,y):
    return (x+y)