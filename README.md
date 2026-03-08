# Projeto de Chat com Sockets e Criptografia

Este projeto foi desenvolvido como atividade prática para a disciplina de Infraestrutura em Redes. É um chat simples de cliente e servidor que usa Sockets TCP e criptografia para proteger as mensagens.

## Tecnologias
* Python 3
* Biblioteca `cryptography` (Fernet)
* Sockets (TCP)

## Como funciona a criptografia
Para este projeto, escolhi a criptografia simétrica **Fernet (AES)**. Usei uma chave única que fica salva tanto no cliente quanto no servidor. 

**O processo é simples:** O cliente pega o que eu digito, transforma em código antes de mandar pela rede e o servidor usa a mesma chave para "traduzir" a mensagem de volta e mostrar na tela. Isso garante que, se alguém interceptar o sinal, só verá códigos bagunçados.

## Como testar
1. Instale a biblioteca: `pip install cryptography`
2. Primeiro, rode o servidor: `python server.py`
3. Depois, abra outro terminal e rode o cliente: `python client.py`
4. Digite a mensagem no cliente e ela aparecerá descriptografada no servidor.

## Arquivos
* `server.py`: Código do servidor que aceita as conexões.
* `client.py`: Código do cliente para enviar mensagens.
* `.gitignore`: Para não subir arquivos inúteis do Python.
