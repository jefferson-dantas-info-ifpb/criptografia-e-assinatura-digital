from criptografia import (
    assinar_mensagem,
    criptografar_mensagem,
    descriptografar_mensagem,
    gerar_chaves,
    verificar_assinatura,
)

chave_publica_ana, chave_privada_ana = gerar_chaves()
chave_publica_joao, chave_privada_joao = gerar_chaves()

print("\nChave pública de Ana:")
print(chave_publica_ana)
print("\nChave privada de Ana:")
print(chave_privada_ana)
print("\nChave pública de João:")
print(chave_publica_joao)
print("\nChave privada de João:")
print(chave_privada_joao)

# Ana vai enviar uma mensagem para João
mensagem = "Oi João, tudo bem?"

mensagem_cript_para_joao = criptografar_mensagem(mensagem, chave_publica_joao)

assinatura_mensagem = assinar_mensagem(mensagem, chave_privada_ana)

print("\nMensagem criptografada para João:")
print(mensagem_cript_para_joao)

print("\nAssinatura da mensagem:")
print(assinatura_mensagem)

mensagem_original = descriptografar_mensagem(
    mensagem_cript_para_joao, chave_privada_joao
)
print("\nMensagem original recebida por João:")
print(mensagem_original)

verifica_assinatura = verificar_assinatura(
    mensagem, assinatura_mensagem, chave_publica_ana
)
print("\nVerificação da assinatura:")
if verifica_assinatura:
    print("Assinatura válida!")
else:
    print("Assinatura inválida!")
