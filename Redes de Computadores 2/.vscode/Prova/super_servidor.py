import socket
import threading

class SuperServidor:
    def __init__(self):
        self.servidores = {}

    def iniciar(self, host, porta):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor_socket:
            servidor_socket.bind((host, porta))
            servidor_socket.listen()

            print(f"Super Servidor ouvindo em {host}:{porta}")

            while True:
                cliente_socket, cliente_endereco = servidor_socket.accept()
                print(f"Conexão TCP recebida de {cliente_endereco}")
                tipo_servidor = cliente_socket.recv(1024).decode()

                if tipo_servidor == "matematica":
                    servidor = threading.Thread(target=self.servidor_matematica, args=(cliente_socket,))
                elif tipo_servidor == "arquivo":
                    servidor = threading.Thread(target=self.servidor_arquivo, args=(cliente_socket,))
                else:
                    cliente_socket.send("Erro: Tipo de serviço inválido".encode())
                    cliente_socket.close()
                    continue

                servidor.start()

    def servidor_matematica(self, cliente_socket):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor_socket:
            servidor_socket.bind(('localhost', 0))  # Use uma porta dinâmica
            servidor_socket.listen()
            cliente_socket.send(f"TCP:{servidor_socket.getsockname()[1]}".encode())
            
            while True:
                cliente_socket, cliente_endereco = servidor_socket.accept()
                print(f"Conexão Matemática recebida de {cliente_endereco}")
                operacao = cliente_socket.recv(1024).decode()

                try:
                    resultado = self.calcular(operacao)
                    cliente_socket.send(str(resultado).encode())
                except Exception as e:
                    cliente_socket.send(str(e).encode())

                cliente_socket.close()

    def servidor_arquivo(self, cliente_socket):
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as servidor_socket:
            servidor_socket.bind(('localhost', 0))  # Use uma porta dinâmica
            cliente_socket.send(f"UDP:{servidor_socket.getsockname()[1]}".encode())
            cliente_socket.close()
            print(f"Servidor de Arquivo ouvindo em localhost:{servidor_socket.getsockname()[1]}")
            while True:
                dados, endereco_cliente = servidor_socket.recvfrom(1024)
                mensagem = dados.decode()
                comando, *argumentos = mensagem.split()

                try:
                    if comando == "criar":
                        nome_arquivo = argumentos[0]
                        with open(nome_arquivo, 'w') as arquivo:
                            arquivo.write("Arquivo criado com sucesso!")
                            resposta = "Arquivo criado com sucesso!"
                    elif comando == "ler":
                        nome_arquivo = argumentos[0]
                        try:
                            with open(nome_arquivo, 'r') as arquivo:
                                resposta = arquivo.read()
                        except FileNotFoundError:
                            resposta = "Arquivo não encontrado"
                    elif comando == "escrever":
                        nome_arquivo = argumentos[0]
                        conteudo = ' '.join(argumentos[1:])
                        with open(nome_arquivo, 'a') as arquivo:
                            arquivo.write(conteudo + "\n")
                        resposta = "Conteúdo adicionado com sucesso!"
                    else:
                        raise ValueError("Comando inválido")

                    servidor_socket.sendto(resposta.encode(), endereco_cliente)
                except Exception as e:
                    servidor_socket.sendto(str(e).encode(), endereco_cliente)

    def calcular(self, operacao):
        partes = operacao.split()
        operador = partes[0]
        numeros = [float(x) for x in partes[1:]]

        if operador == '+':
            return sum(numeros)
        elif operador == '-':
            return numeros[0] - sum(numeros[1:])
        elif operador == '*':
            resultado = 1
            for num in numeros:
                resultado *= num
            return resultado
        elif operador == '/':
            resultado = numeros[0]
            for num in numeros[1:]:
                resultado /= num
            return resultado
        elif operador == 'media':
            return sum(numeros) / len(numeros)
        else:
            raise ValueError("Operação inválida")

if __name__ == "__main__":
    super_servidor = SuperServidor()
    super_servidor.iniciar('localhost', 8080)
