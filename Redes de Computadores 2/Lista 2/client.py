import socket
import time

# Configurações do cliente
HOST = 'server'
PORT = 65432

# Inicia o socket do cliente TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    for i in range(1000):
        # Marca o tempo de envio
        sent_time = time.time()
        
        # Envia o tempo de envio ao servidor
        s.sendall(str(sent_time).encode())
        
        time.sleep(0.01)
        
