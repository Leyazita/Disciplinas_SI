import socket

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def handle_client(conn, addr):
    print(f"Conexão de {addr}")
    data = conn.recv(1024).decode()
    if data.isdigit():
        year = int(data)
        response = f"{year} é bissexto" if is_leap_year(year) else f"{year} não é bissexto"
    else:
        response = "Entrada inválida."
    conn.sendall(response.encode())
    conn.close()

def main():
    host = "127.0.0.1"
    port = 12346
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print("Servidor sequencial rodando...")
    
    while True:
        conn, addr = server_socket.accept()
        handle_client(conn, addr)

if __name__ == "__main__":
    main()
