def app(environ, start_response):
    """Simplest possible application object"""
    dados=open("mix.html", mode="r")
    bytes(dados)
    data=dados.read()
    status = '200 OK'
    headers = [('Content-type', 'text/html')]
    start_response(status, headers)
    return [data]

def somar(x,y):
    return (x+y)