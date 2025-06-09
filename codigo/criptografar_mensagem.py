import rsa
import base64

mensagem = input("Digite a mensagem a ser criptografada: ")

with open("chaves/chave_publica_a.pem", mode='rb') as f:
    chave_publica_a_pem = f.read()

with open("chaves/chave_privada_b.pem", mode='rb') as f:
    chave_privada_b_pem = f.read()

chave_publica_a = rsa.PublicKey.load_pkcs1(chave_publica_a_pem)
chave_privada_b = rsa.PrivateKey.load_pkcs1(chave_privada_b_pem)

mensagem_criptografada = rsa.encrypt(mensagem.encode(), chave_publica_a)
mensagem_cripto_base64 = base64.b64encode(mensagem_criptografada).decode()
assinatura = rsa.sign(mensagem.encode(), chave_privada_b, 'SHA-1')
assinatura_base64 = base64.b64encode(assinatura).decode()

print("Mensagem criptografada: " + mensagem_cripto_base64)
print("Assinatura: " + assinatura_base64)

with open("mensagens/mensagem.txt", "w") as f:
  f.write(mensagem)

with open("mensagens/mensagem_cripto.txt", "w") as f:
  f.write(mensagem_cripto_base64)

with open("mensagens/assinatura.bin", "w") as f:
  f.write(assinatura_base64)
