import socket
import threading
from cryptography.fernet import Fernet

# CHAVE DE CRIPTOGRAFIA (Deve ser a mesma no cliente e servidor)
# Em um sistema real, isso seria uma variável de ambiente
CHAVE = b'y7_L7vW48W2-Z8Z-Lq7-88Ym6f9a5_8B8_8_8_8_8_8='
cipher_suite = Fernet(CHAVE)


def handle_client(client_socket, addr):
    print(f"[NOVA CONEXÃO] {addr} conectado.")
    while True:
        try:
            # Recebe os bytes criptografados
            msg_criptografada = client_socket.recv(1024)
            if not msg_criptografada:
                break

            # Descriptografa e converte para string
            msg_decriptada = cipher_suite.decrypt(
                msg_criptografada).decode('utf-8')
            print(f"[{addr}] Mensagem Recebida: {msg_decriptada}")

        except Exception as e:
            print(f"[ERRO] Conexão com {addr} encerrada.")
            break
    client_socket.close()


def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 5000))
    server.listen()
    print("[AGUARDANDO] Servidor rodando em localhost:5000...")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()


if __name__ == "__main__":
    start_server()
