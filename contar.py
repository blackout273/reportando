def app(environ, start_response):
    """Simplest possible application object"""

    data = b"<html lang='pt-br'>    " \
           b"<head>    " \
           b"<meta charset='utf-8'>    " \
           b"<title>Pipeline</title>    " \
           b"<style>    " \
           b"*{    " \
           b"margin:0;    " \
           b"padding:0;    " \
           b"}    " \
           b".container{    " \
           b"position:absolute;    " \
           b"margin-left:50%;    " \
           b"transform:translateX(-50%);    " \
           b"margin-top:15%;    " \
           b"font-size:2vw;    " \
           b"text-align:center;" \
           b"}    " \
           b".btn{        " \
           b"border: none;        " \
           b"background-color: white;        " \
           b"color: black;        " \
           b"width: 2vw;        " \
           b"height: 2vh;        " \
           b"border-radius: 10px;        " \
           b"transition: 0.5s ease;    " \
           b"}    " \
           b".btn:hover{        " \
           b"background-color: black;        " \
           b"color: white;        " \
           b"border: 2px solid white;        " \
           b"transition: 0.3s ease;    " \
           b"}    " \
           b"body{        " \
           b"transition: 0.5s ease;        " \
           b"font-family: 'Courier New', Courier, monospace;    " \
           b"}    " \
           b"body:hover{        " \
           b"background-color: black;        " \
           b"color: white;        " \
           b"transition: 0.3s ease;    " \
           b"}    " \
           b"</style>" \
           b"</head>    " \
           b"<body>    " \
           b"<div class='container'><h3>Calcule o seu indice de Massa Corporal(IMC)</h3>    " \
           b"<h6 id='cobaia'></h6><br>    " \
           b"<input type='number' id='peso' placeholder='Peso' style='text-align: center;width: 10vw;height: 2vh;'><br><br>    " \
           b"<input type='number' id='altura' placeholder='Altura , em centimetros' style='text-align: center;width: 10vw;height: 2vh;'><br><br>    " \
           b"<button type='submit' class='btn' onclick=(botao())>GO</button>     " \
           b"</div>    " \
           b"</body>    " \
           b"<footer> <script type='text/javascript'>" \
           b"var peso = document.getElementById('peso');" \
           b"var altura = document.getElementById('altura');" \
           b"function botao(){" \
           b"var imc = peso.value/(altura.value*altura.value)*10000;" \
           b"alert('IMC: '+imc);" \
           b"if(imc<18.50){" \
           b"document.getElementById('cobaia').innerHTML='<h6>Class: Magreza - Obesidade grau 0<h6>'}" \
           b"if(imc>=18.50 && imc<=24.9){document.getElementById('cobaia').innerHTML='<h6>Class: Normal - Obesidade grau 0<h6>'}" \
           b"if(imc>=25.00 && imc<=29.90){document.getElementById('cobaia').innerHTML='<h6>Class: Sobrepeso - Obesidade grau 1<h6> ' }" \
           b"if(imc>=30.00 && imc<=39.90){document.getElementById('cobaia').innerHTML='<h6>Class: Obesidade - Obesidade grau 2<h6>'}" \
           b"if(imc>=40.00){document.getElementById('cobaia').innerHTML='<h6>Class: Obesidade Grave - Obesidade grau 3<h6>'" \
           b"}" \
           b"}    " \
           b"</script>    " \
           b"</footer>    " \
           b"</html>    "

    status = '200 OK'
    headers = [('Content-type', 'text/html')]
    start_response(status, headers)
    return [data]


def somar(x, y):
    return (x + y)
