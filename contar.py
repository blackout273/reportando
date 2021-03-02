def app(environ, start_response):
    """Simplest possible application object"""
    data = b"<h1>Fim da pipeline</h1><button id='btn' type='submit'>enviar</button><script>btn = document.getElementsById('btn') if(btn){alert('apertou botao')}</script>"
    status = '200 OK'
    headers = [('Content-type', 'text/html')]
    start_response(status, headers)
    return [data]

def somar(x,y):
    return (x+y)