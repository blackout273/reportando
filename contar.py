def app(environ, start_response):
    """Simplest possible application object"""

    data = b"<html lang='pt-br'>    <head>    <meta charset='utf-8'>    <title>Pipeline</title>    <style>    *{    margin:0;    padding:0;    }    .container{    position:absolute;    margin-left:50%;    transform:translateX(-50%);    margin-top:15%;    font-size:2vw;    text-align:center;}    .btn{        border: none;        background-color: white;        color: black;        width: 2vw;        height: 2vh;        border-radius: 10px;        transition: 0.5s ease;    }    .btn:hover{        background-color: black;        color: white;        border: 2px solid white;        transition: 0.3s ease;    }    body{        transition: 0.5s ease;        font-family: 'Courier New', Courier, monospace;    }    body:hover{        background-color: black;        color: white;        transition: 0.3s ease;    }    </style></head>    <body>    <div class='container'><h3>Calcule o seu indice de Massa Corporal(IMC)</h3>    <h6 id='cobaia'></h6><br>    <input type='number' id='peso' placeholder='Peso' style='text-align: center;width: 10vw;height: 2vh;'><br><br>    <input type='number' id='altura' placeholder='Altura , em centimetros' style='text-align: center;width: 10vw;height: 2vh;'><br><br>    <button type='submit' class='btn' onclick=(botao())>GO</button>     </div>    </body>    <footer> <script type='text/javascript'>var peso = document.getElementById('peso')var altura = document.getElementById('altura')function botao(){var imc = peso.value/(altura.value*altura.value)*10000alert('IMC: '+imc)if(imc<18.50){document.getElementById('cobaia').innerHTML='<h6>Classi: Magreza - Obesidade grau 0<h6>'}if(imc>=18.50 && imc<=24.9){document.getElementById('cobaia').innerHTML='<h6>Classi: Normal - Obesidade grau 0<h6>'}if(imc>=25.00 && imc<=29.90){document.getElementById('cobaia').innerHTML='<h6>Classi: Sobrepeso - Obesidade grau 1<h6> ' }if(imc>=30.00 && imc<=39.90){document.getElementById('cobaia').innerHTML='<h6>Classi: Obesidade - Obesidade grau 2<h6>'}if(imc>=40.00){document.getElementById('cobaia').innerHTML='<h6>Classi: Obesidade Grave - Obesidade grau 3<h6>'}}    </script>    </footer>    </html>    "

    status = '200 OK'
    headers = [('Content-type', 'text/html')]
    start_response(status, headers)
    return [data]


def somar(x, y):
    return (x + y)
