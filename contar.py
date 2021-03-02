def app(environ, start_response):
    """Simplest possible application object"""
    data = b'<!DOCTYPE html>'
    b'<html lang="pt-br">'
    b'<head>'
    b'<title>Pipeline</title>'
    b'<style>'
    b'*{'
    b'margin:0;'
    b'padding:0;'
    b'}'
    b'.container{'
    b'position:absolute;'
    b'margin-left:50%;'
    b'transform:translateX(-50%);'
    b'margin-top:15%;'
    b'font-size:2vw;'
    b'text-align:center;'
    b'}'
    b'</style>'
    b'</head>'
    b'<body>'
    b'<div class="container">'
    b'<h1>Pipeline Completa</h1>'
    b'<h6>por favor insira o seu nome</h6>'
    b'<input type="text" id="nome" placeholder="Por favor, insira o seu nome">'
    b'<button type="submit" onclick=(botao())>enviar</button> '
    b'</div>'
    b'</body>'
    b'<script type="text/javascript">'
    b'var nome = document.getElementById("nome");'
    b'function botao(){'
    b'alert(+nome.value);'
    b'}'
    b'</script>'
    b'</html>'
    str(data).encode('utf-8')
    status = '200 OK'
    headers = [('Content-type', 'text/html')]
    start_response(status, headers)
    return [data]

def somar(x,y):
    return (x+y)