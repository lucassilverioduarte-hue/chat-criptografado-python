Arquitetura: Cliente-Servidor via TCP. O TCP foi escolhido por garantir que os pacotes de mensagens cheguem na ordem correta e sem perdas.

Criptografia Simétrica (AES/Fernet): Utilizamos a biblioteca cryptography com o protocolo Fernet. Ele usa AES no modo CBC com uma chave de 128 bits para criptografia e HMAC para autenticação (garante que a mensagem não foi alterada).

Fluxo de Dados:

O Cliente transforma a string em bytes (utf-8).

A chave simétrica embaralha esses bytes.

O Servidor recebe os bytes embaralhados e usa a mesma chave para reverter o processo.