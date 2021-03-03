import socket
def app(environ, start_response):
    """Simplest possible application object"""
    host=socket.gethostbyname(socket.gethostname())
    port = 8080
    addr=(host,port)
    data = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    data.bind((addr))
    data.listen(1)
    while True:
        conn,host=data.accept()
        print(" Conectado a : ", host)
        status = '200 OK'
        while True:
            headers = [('Content-type', 'text/html')]
            start_response(status, headers)
            if not conn: break
        print("conexao finalizada")
        conn.close()
        return [data]


def somar(x,y):
    return (x+y)

