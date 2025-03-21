import socket
import threading
import uuid
import time

class SuperServidor:
    def __init__(self, host, porta):
        self.host = host
        self.porta = porta
        self.servidores_tcp = {}
        self.servidores_udp = {}
        self.threads_servidor = {}

    def iniciar(self):
        print(f"Iniciando Super Servidor TCP em {self.host}:{self.porta}...")
        self.soquete = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.soquete.bind((self.host, self.porta))
        self.soquete.listen()
        self.soquete.settimeout(1) 
        while True:  
            try:
                soquete_cliente, endereco_cliente = self.soquete.accept()
                threading.Thread(target=self.lidar_com_cliente, args=(soquete_cliente,)).start()
            except socket.timeout:
                continue

    def lidar_com_cliente(self, soquete_cliente):
        while True:
            requisicao = soquete_cliente.recv(1024).decode('utf-8')
            if not requisicao:
                break
            elif requisicao == "DESATIVAR":
                print("Desativando Super Servidor...")
                self.parar()
                break
            elif requisicao == "CRIAR TCP":
                porta_tcp_servidor = self.criar_servidor_tcp()
                soquete_cliente.sendall(str(porta_tcp_servidor).encode('utf-8'))
            elif requisicao == "CRIAR UDP":
                porta_udp_servidor = self.criar_servidor_udp()
                soquete_cliente.sendall(str(porta_udp_servidor).encode('utf-8'))
            elif requisicao == "LISTAR SERVIDORES":
                resposta = self.listar_servidores()
                soquete_cliente.sendall(resposta.encode('utf-8'))
            elif requisicao.startswith("ENCERRAR "):
                id_servidor = requisicao[len("ENCERRAR "):]
                resposta = self.encerrar_servidor(id_servidor)
                soquete_cliente.sendall(resposta.encode('utf-8'))
            else:
                soquete_cliente.sendall("Requisição inválida".encode('utf-8'))
        soquete_cliente.close()

    def criar_servidor_tcp(self):
        id_servidor = str(uuid.uuid4())
        porta = self.encontrar_porta_disponivel()
        self.servidores_tcp[id_servidor] = porta
        threading.Thread(target=self.iniciar_servidor_tcp, args=(porta,)).start()
        return porta

    def iniciar_servidor_tcp(self, porta):
        print(f"Servidor TCP ouvindo em localhost:{porta}...")
        soquete_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        soquete_servidor.bind(('localhost', porta))
        soquete_servidor.listen()
        self.threads_servidor[porta] = threading.Thread(target=self.lidar_com_cliente_tcp, args=(soquete_servidor,))
        self.threads_servidor[porta].start()

    def lidar_com_cliente_tcp(self, soquete_servidor):
        while True:
            soquete_cliente, _ = soquete_servidor.accept()
            requisicao = soquete_cliente.recv(1024).decode('utf-8')
            if not requisicao:
                break
            try:
                resultado = eval(requisicao)
                soquete_cliente.sendall(str(resultado).encode('utf-8'))
            except Exception as e:
                soquete_cliente.sendall(f"Erro ao calcular a expressão: {e}".encode('utf-8'))
        soquete_servidor.close()

    def criar_servidor_udp(self):
        id_servidor = str(uuid.uuid4())
        porta = self.encontrar_porta_disponivel()
        self.servidores_udp[id_servidor] = porta
        threading.Thread(target=self.iniciar_servidor_udp, args=(porta,)).start()
        return porta

    def iniciar_servidor_udp(self, porta):
        print(f"Servidor UDP ouvindo em localhost:{porta}...")
        soquete_servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        soquete_servidor.bind(('localhost', porta))
        while True:
            dados, addr = soquete_servidor.recvfrom(1024)
            threading.Thread(target=self.lidar_com_cliente_udp, args=(dados, addr, soquete_servidor)).start()

    def lidar_com_cliente_udp(self, dados, addr, soquete_servidor):
        requisicao = dados.decode('utf-8')
        if requisicao.startswith("ENVIAR "):
            nome_arquivo = requisicao[len("ENVIAR "):]
            try:
                with open(nome_arquivo, 'rb') as arquivo:
                    while True:
                        chunk = arquivo.read(1024)
                        if not chunk:
                            break
                        soquete_servidor.sendto(chunk, addr)
                print(f"Arquivo '{nome_arquivo}' enviado com sucesso.")
            except Exception as e:
                print(f"Erro ao enviar arquivo: {e}")
        elif requisicao.startswith("RECEBER "):
            nome_arquivo = requisicao[len("RECEBER "):]
            try:
                with open(nome_arquivo, 'rb') as arquivo:
                    while True:
                        chunk = arquivo.read(1024)
                        if not chunk:
                            break
                        soquete_servidor.sendto(chunk, addr)
                    soquete_servidor.sendto(b"FIM DO ARQUIVO", addr)
                    print(f"Arquivo '{nome_arquivo}' enviado com sucesso.")
            except Exception as e:
                print(f"Erro ao enviar arquivo: {e}")
        else:
            print("Requisição inválida")

    def parar(self):
        self.soquete.close()
        for porta, thread in self.threads_servidor.items():
            thread.join()

    def encontrar_porta_disponivel(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('localhost', 0))
        porta = s.getsockname()[1]
        s.close()
        return porta

    def listar_servidores(self):
        servidores = "Servidores:\n"
        servidores += "Servidores TCP:\n"
        for id_servidor, porta in self.servidores_tcp.items():
            servidores += f"  ID: {id_servidor}, Porta: {porta}, Tipo: TCP\n"
        servidores += "Servidores UDP:\n"
        for id_servidor, porta in self.servidores_udp.items():
            servidores += f"  ID: {id_servidor}, Porta: {porta}, Tipo: UDP\n"
        return servidores

    def encerrar_servidor(self, id_servidor):
        if id_servidor in self.servidores_tcp:
            del self.servidores_tcp[id_servidor]
            return f"Servidor TCP com ID: {id_servidor} foi encerrado."
        elif id_servidor in self.servidores_udp:
            del self.servidores_udp[id_servidor]
            return f"Servidor UDP com ID: {id_servidor} foi encerrado."
        else:
            return f"Nenhum servidor encontrado com ID: {id_servidor}"

if __name__ == "__main__":
    porta = 9000  # Porta TCP fixa
    super_servidor = SuperServidor('localhost', porta)
    super_servidor.iniciar()
