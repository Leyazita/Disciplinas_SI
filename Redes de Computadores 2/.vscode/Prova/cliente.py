import socket

class Cliente:
    def __init__(self, super_servidor_host, super_servidor_porta):
        self.super_servidor_host = super_servidor_host
        self.super_servidor_porta = super_servidor_porta

    def conectar_super_servidor(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente_socket:
            try:
                cliente_socket.connect((self.super_servidor_host, self.super_servidor_porta))
            except ConnectionError as e:
                print("Erro ao conectar ao servidor:", e)
                return

            while True:
                tipo_servidor = input("Digite 'matematica' ou 'arquivo': ")
                cliente_socket.send(tipo_servidor.encode())

                try:
                    mensagem_servidor = cliente_socket.recv(1024).decode()
                    print(mensagem_servidor)
                except ConnectionAbortedError:
                    print("Conexão interrompida pelo servidor.")
                    break

                print(mensagem_servidor)

                if mensagem_servidor.startswith("Erro"):
                    print("Erro:", mensagem_servidor)
                    continue

                # Receber o tipo de serviço (TCP ou UDP) do servidor
                tipo_servico = cliente_socket.recv(1024).decode()

                if tipo_servico == "TCP":
                    servidor_credenciais = cliente_socket.recv(1024).decode().split(":")
                    if len(servidor_credenciais) != 2:
                        print("Erro: Credenciais do servidor inválidas.")
                        continue

                    servidor_host, servidor_porta = servidor_credenciais
                    servidor_porta = int(servidor_porta)

                    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor_socket:
                        try:
                            servidor_socket.connect((servidor_host, servidor_porta))
                        except ConnectionError as e:
                            print("Erro ao conectar ao servidor:", e)
                            continue

                        if tipo_servidor == "matematica":
                            self.servico_matematica(servidor_socket)
                        elif tipo_servidor == "arquivo":
                            self.servico_arquivo(servidor_socket)
                
                elif tipo_servico == "UDP":
                    if tipo_servidor == "arquivo":
                        self.servico_arquivo_udp(cliente_socket)
                
                else:
                    print("Tipo de serviço desconhecido.")
                    continue

    def servico_matematica(self, servidor_socket):
        while True:
            operacao = input("Digite a operação (ex: '+ 2 3', 'media 4 5 6'): ")
            servidor_socket.send(operacao.encode())

            resultado = servidor_socket.recv(1024).decode()
            print("Resultado:", resultado)

            continuar = input("Deseja fazer outra operação? (s/n): ")
            if continuar.lower() != 's':
                break

    def servico_arquivo(self, servidor_socket):
        while True:
            comando = input("Digite o comando (criar/nome_arquivo, ler/nome_arquivo, escrever/nome_arquivo conteudo): ")
            servidor_socket.send(comando.encode())

            resposta = servidor_socket.recv(1024).decode()
            print("Resposta do servidor:", resposta)

            continuar = input("Deseja fazer outra operação? (s/n): ")
            if continuar.lower() != 's':
                break

    def servico_arquivo_udp(self, cliente_socket):
        while True:
            comando = input("Digite o comando (criar/nome_arquivo, ler/nome_arquivo, escrever/nome_arquivo conteudo): ")
            cliente_socket.send(comando.encode())

            resposta, _ = cliente_socket.recvfrom(1024)
            print("Resposta do servidor:", resposta.decode())

            continuar = input("Deseja fazer outra operação? (s/n): ")
            if continuar.lower() != 's':
                break

if __name__ == "__main__":
    cliente = Cliente('localhost', 8080)
    cliente.conectar_super_servidor()