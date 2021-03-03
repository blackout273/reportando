def app(environ, start_response):
    """Simplest possible application object"""

    data = b"<!DOCTYPE html>" \
           b"<html=lang'pt-br'>" \
           b"<head><title>Pipeline</title>" \
           b"<style>*{" \
           b"margin:0;padding:0;}" \
           b".container{position:absolute;margin-left:50%;transform:translateX(-50%);margin-top:15%;font-size:2vw;text-align:center;}" \
           b"</style></head>" \
           b"<body>" \
           b"<div class='container'><h1>Pipeline Completa</h1>" \
           b"<h6>por favor insira o seu nome</h6>" \
           b"<input type='text' id='nome' placeholder='Por favor, insira o seu nome'>" \
           b"<button type='submit' onclick=(botao())>enviar</button>" \
           b" </div>" \
           b"</body>" \
           b"<script type='text/javascript'>" \
           b"var nome = document.getElementById('nome');" \
           b"function botao(){" \
           b"alert('ola: '+nome.value);" \
           b"}</script>" \
           b"</html>"

    status = '200 OK'
    headers = [('Content-type', 'text/html')]
    start_response(status, headers)
    return [data]


def somar(x, y):
    return (x + y)
