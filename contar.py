def app(environ, start_response):
    """Simplest possible application object"""
    dados=open("index.html", mode="r")
    data=dados.read()
    bytes(data, encoding='utf8')
    status = '200 OK'
    headers = [('Content-type', 'text/html')]
    start_response(status, headers)
    return [data]

def somar(x,y):
    return (x+y)