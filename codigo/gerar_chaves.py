import rsa
import os.path

existe_chave_publica = os.path.isfile("chaves/chave_publica_b.pem")
existe_chave_privada = os.path.isfile("chaves/chave_privada_b.pem")

if existe_chave_publica or existe_chave_privada:
  resposta = input("Existem chaves já geradas, gerar outras? (y/N) ")
  if resposta.lower() != "y":
    raise Exception("Cancelado")

chave_publica, chave_privada = rsa.newkeys(512)

with open("chaves/chave_publica_b.pem", "w") as f:
  f.write(chave_publica.save_pkcs1().decode())

with open("chaves/chave_privada_b.pem", "w") as f:
  f.write(chave_privada.save_pkcs1().decode())




