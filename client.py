import socket
from cryptography.fernet import Fernet

# A CHAVE DEVE SER IDÊNTICA À DO SERVIDOR
CHAVE = b'y7_L7vW48W2-Z8Z-Lq7-88Ym6f9a5_8B8_8_8_8_8_8='
cipher_suite = Fernet(CHAVE)


def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 5000))
    print("[CONECTADO] Digite suas mensagens (ou 'sair' para encerrar):")

    while True:
        msg = input("> ")
        if msg.lower() == 'sair':
            break

        # Criptografa a mensagem antes de enviar
        msg_criptografada = cipher_suite.encrypt(msg.encode('utf-8'))
        client.send(msg_criptografada)

    client.close()


if __name__ == "__main__":
    start_client()
