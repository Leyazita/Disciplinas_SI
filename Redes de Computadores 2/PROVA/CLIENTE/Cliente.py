import socket
import time
import os

class Cliente:
    def __init__(self, host, porta, protocolo):
        self.host = host
        self.porta = porta
        self.protocolo = protocolo
        self.soquete = None

    def conectar(self):
        if self.soquete:
            self.soquete.close()
        self.soquete = socket.socket(socket.AF_INET, socket.SOCK_STREAM if self.protocolo == 'tcp' else socket.SOCK_DGRAM)
        self.soquete.connect((self.host, self.porta))

    def enviar_requisicao(self, requisicao, decodificar=True):
        if self.soquete:
            self.soquete.sendall(requisicao.encode('utf-8'))
            resposta = self.soquete.recv(1024)
            if decodificar:
                resposta = resposta.decode('utf-8')
            return resposta
        else:
            return "Erro: Socket não conectado."

    def enviar_dados(self, dados):
        if self.soquete:
            self.soquete.sendall(dados)
        else:
            print("Erro: Socket não conectado.")

    def fechar_conexao(self):
        if self.soquete:
            self.soquete.close()

    def receber_arquivo(self, nome_arquivo):
        try:
            caminho_arquivo = os.path.join(os.path.dirname(os.path.abspath(__file__)), "downloads", nome_arquivo)
            with open(caminho_arquivo, 'wb') as arquivo:
                while True:
                    pedaco = self.soquete.recv(1024)
                    if pedaco == b"FIM DO ARQUIVO":  
                        break
                    arquivo.write(pedaco)
            return True, f"Arquivo '{nome_arquivo}' recebido e salvo com sucesso em '{caminho_arquivo}'."
        except Exception as e:
            print("Erro ao receber arquivo:", e)
            return False, f"Erro ao receber arquivo: {e}"


def criar_servidor(super_servidor_cliente, tipo_servidor):
    protocolo = 'tcp' if tipo_servidor.lower() == 'matemática' else 'udp'
    resposta = super_servidor_cliente.enviar_requisicao(f"CRIAR {protocolo.upper()}")
    print("Resposta:", resposta)
    
    if resposta:
        time.sleep(0.5)
        host_servidor = super_servidor_cliente.host
        porta_servidor = int(resposta)
        cliente_servidor = Cliente(host_servidor, porta_servidor, protocolo)
        cliente_servidor.conectar()
        print(f"Conectado ao servidor de {tipo_servidor.upper()}.")
        return cliente_servidor
    else:
        return None

def lidar_com_servidor_matematica(cliente_servidor):
    while True:
        msg = input("Digite uma expressão matemática (digite 'sair' para sair): ")
        if msg.lower() == 'sair':
            cliente_servidor.fechar_conexao()
            break
        else:
            resposta = cliente_servidor.enviar_requisicao(msg)
            print("Resultado da operação:", resposta)

def lidar_com_servidor_arquivo(cliente_servidor):
    while True:
        comando = input("Digite 'enviar' para enviar um arquivo, 'baixar' para baixar um arquivo, ou 'sair' para sair: ")
        if comando.lower() == 'sair':
            cliente_servidor.fechar_conexao()
            break
        elif comando.lower() == 'enviar':
            nome_arquivo = input("Digite o nome do arquivo a ser enviado: ")
            try:
                with open(f'Cliente/{nome_arquivo}', 'rb') as arquivo:
                    while True:
                        pedaco = arquivo.read(1024)
                        if not pedaco:
                            break
                        cliente_servidor.enviar_dados(pedaco)
                print(f"Arquivo '{nome_arquivo}' enviado com sucesso.")
            except Exception as e:
                print(f"Erro ao enviar arquivo: {e}")
        elif comando.lower() == 'baixar':
            nome_arquivo = input("Digite o nome do arquivo a ser baixado: ")
            cliente_servidor.enviar_requisicao("RECEBER " + nome_arquivo, decodificar=False)
            sucesso, mensagem = cliente_servidor.receber_arquivo(nome_arquivo)
            if sucesso:
                print(mensagem)
            else:
                print("Erro ao receber arquivo:", mensagem)
        else:
            print("Comando inválido. Por favor, digite 'enviar', 'baixar' ou 'sair'.")


if __name__ == "__main__":
    host_super_servidor = 'localhost'
    porta_super_servidor = 9000
    super_servidor_cliente = Cliente(host_super_servidor, porta_super_servidor, 'tcp')
    super_servidor_cliente.conectar()

    while True:
        comando = input("Digite 'matemática' para criar um servidor de matemática,\n 'arquivo' para criar um servidor de arquivo,\n\
            'listar' para listar os servidores,\n 'encerrar' para encerrar um servidor,\n ou 'sair' para sair: ")
        if comando.lower() in ['matemática', 'arquivo']:
            cliente_servidor = criar_servidor(super_servidor_cliente, comando)
            if cliente_servidor:
                if comando.lower() == 'matemática':
                    lidar_com_servidor_matematica(cliente_servidor)
                else:
                    lidar_com_servidor_arquivo(cliente_servidor)
        elif comando.lower() == 'listar':
            resposta = super_servidor_cliente.enviar_requisicao("LISTAR SERVIDORES")
            print("Resposta:", resposta)
        elif comando.lower() == 'encerrar':
            id = input("Digite o ID do servidor para encerrar: ")
            resposta = super_servidor_cliente.enviar_requisicao(f"ENCERRAR {id}")
            print("Resposta:", resposta)
        elif comando.lower() == 'sair':
            print("Saindo...")
            super_servidor_cliente.enviar_requisicao("DESATIVAR")
            super_servidor_cliente.fechar_conexao()
            break
        else:
            print("Entrada inválida. Por favor, digite 'matemática', 'arquivo', 'listar', 'encerrar' ou 'sair'.")
