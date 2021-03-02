def app(environ, start_response):
    """Simplest possible application object"""
    status = input("Insira uma frase")
    data = status.encode('utf-8')
    headers = [('Content-type', 'text/html')]
    start_response(status, headers)
    return [data]

def somar(x,y):
    return (x+y)