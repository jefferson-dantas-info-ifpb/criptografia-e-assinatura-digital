import rsa
import base64

mensagem_recebida_base64 = input("Digite a mensagem a ser descriptografada: ")

with open("chaves/chave_privada_b.pem", mode='rb') as f:
    chave_privada_b_pem = f.read()

with open("mensagens/assinatura.bin", mode='rb') as f:
    assinatura_base64 = f.read()

with open("chaves/chave_publica_b.pem", mode='rb') as f:
    chave_publica_b_pem = f.read()

mensagem_recebida = base64.b64decode(mensagem_recebida_base64)
assinatura = base64.b64decode(assinatura_base64)

chave_privada_b = rsa.PrivateKey.load_pkcs1(chave_privada_b_pem)
chave_publica_b = rsa.PublicKey.load_pkcs1(chave_publica_b_pem)

mensagem_descriptografada = rsa.decrypt(mensagem_recebida, chave_privada_b).decode()

print("Mensagem descriptografada: " + mensagem_descriptografada)

algoritmo_assinatura = rsa.verify(mensagem_descriptografada.encode(), assinatura, chave_publica_b)

print('Assinatura válida, algoritmo: ' + algoritmo_assinatura)

with open("mensagens/mensagem_recebida.txt", "w") as f:
  f.write(mensagem_descriptografada)
