def app(environ, start_response):
    """Simplest possible application object"""
    data = b"<!DOCTYPE html><html=lang'pt-br'><head><title>Pipeline</title><style>*{margin:0;padding:0;}.container{position:absolute;margin-left:50%;transform:translateX(-50%);margin-top:15%;font-size:2vw;text-align:center;}</style></head><body><div class='container'><h1>Pipeline Completa</h1><h6>por favor insira o seu nome</h6><input type='text' id='nome' placeholder='Por favor, insira o seu nome'><button type='submit' onclick=(botao())>enviar</button> </div></body><script type='text/javascript'>var nome = document.getElementById('nome');function botao(){alert('ola'+nome.value);}</script></html>"
    status = '200 OK'
    headers = [('Content-type', 'text/html')]
    start_response(status, headers)
    return [data]

def somar(x,y):
    return (x+y)