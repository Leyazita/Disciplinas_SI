import socket
import threading
import mimetypes
import os
import logging

# Configuração do logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def process_request(client_socket, client_address):
    """
    Processa a requisição HTTP recebida do cliente.
    """
    try:
        request = client_socket.recv(1024).decode('utf-8')
        
        if not request:
            return
        
        request_lines = request.split('\r\n')
        request_line = request_lines[0]

        try:
            method, path, _ = request_line.split()
        except ValueError:
            send_http_response(client_socket, "400 Bad Request", "Bad Request")
            return

        if method != 'GET':
            send_http_response(client_socket, "405 Method Not Allowed", "Method Not Allowed")
            return
        
        if path == '/':
            path = '/index.html'

        file_path = os.path.join('.', path.lstrip('/'))

        if not os.path.isfile(file_path):
            send_http_response(client_socket, "404 Not Found", "File Not Found")
            return

        if not os.access(file_path, os.R_OK):
            send_http_response(client_socket, "403 Forbidden", "Access Denied")
            return

        send_file_content(client_socket, file_path)
    except Exception as e:
        logging.error(f"Erro ao processar a requisição de {client_address}: {e}")
        send_http_response(client_socket, "500 Internal Server Error", "Internal Server Error")
    finally:
        client_socket.close()

def send_http_response(client_socket, status_code, message):
    """
    Envia uma resposta HTTP com o status e mensagem especificados.
    """
    response = f"HTTP/1.1 {status_code}\r\n\r\n{message}"
    client_socket.sendall(response.encode('utf-8'))

def send_file_content(client_socket, file_path):
    """
    Envia o conteúdo do arquivo solicitado como resposta HTTP.
    """
    mime_type, _ = mimetypes.guess_type(file_path)
    if mime_type is None:
        mime_type = 'application/octet-stream'

    with open(file_path, 'rb') as file:
        file_content = file.read()

    headers = (
        f"HTTP/1.1 200 OK\r\n"
        f"Content-Type: {mime_type}\r\n"
        f"Content-Length: {len(file_content)}\r\n\r\n"
    )

    client_socket.sendall(headers.encode('utf-8') + file_content)

def run_parallel_server(host, port):
    """
    Inicializa o servidor e começa a escutar por conexões.
    """
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    logging.info(f"Servidor paralelo rodando em http://{host}:{port}/")

    try:
        while True:
            client_socket, client_address = server_socket.accept()
            logging.info(f"Nova conexão de {client_address[0]}:{client_address[1]}")
            
            # Processar a requisição em uma nova thread
            threading.Thread(target=process_request, args=(client_socket, client_address)).start()
    except KeyboardInterrupt:
        logging.info("Servidor interrompido pelo usuário")
    finally:
        server_socket.close()

if __name__ == "__main__":
    run_parallel_server('0.0.0.0', 8081)
