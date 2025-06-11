from utils import arquivo_existe, ler_arquivo, print_aviso, print_erro, print_sucesso, salvar_arquivo
from colorama import Fore as F
from criptografia import (
    assinar_mensagem,
    descriptografar_mensagem,
    gerar_chaves,
    criptografar_mensagem,
    verificar_assinatura,
)


def gerar_chaves_e_guardar():
    chave_existente = verificar_chave_existente()
    if chave_existente:
        return

    print("Gerando chaves...")
    chave_publica_pem, chave_privada_pem = gerar_chaves()
    salvar_arquivo("particular/minha_chave_publica.pem", chave_publica_pem)
    salvar_arquivo("particular/minha_chave_privada.pem", chave_privada_pem)
    salvar_arquivo("enviar/chave_publica.pem", chave_publica_pem)
    print_sucesso("Chaves geradas com sucesso!")


def verificar_chave_existente():
    existe_publica = arquivo_existe("particular/minha_chave_publica.pem")
    existe_privada = arquivo_existe("particular/minha_chave_privada.pem")
    if not existe_publica and not existe_privada:
        return False

    resposta = input("Já existem chaves geradas. Deseja gerar novas chaves? (s/N): ")
    if resposta.strip().lower() == "s":
        return False
    else:
        print_aviso("Cancelado")
        return True


def criptografar():
    chave_publica_existe = arquivo_existe("recebido/chave_publica.pem")
    minha_chave_privada_existe = arquivo_existe("particular/minha_chave_privada.pem")

    if not chave_publica_existe:
        print_erro("Chave pública não encontrada. Peça ao seu parceiro para enviar a chave pública dele.")
        print_erro("Coloque a chave pública recebida em 'recebido/chave_publica.pem'")
        return

    if not minha_chave_privada_existe:
        print_erro("Chave privada não encontrada. Gere suas chaves primeiro.")
        return

    chave_publica = ler_arquivo("recebido/chave_publica.pem")
    mensagem = input("Digite a mensagem a ser criptografada: ")
    print("\nCriptografando mensagem...")
    mensagem_criptografada = criptografar_mensagem(mensagem, chave_publica)
    print_sucesso("Mensagem criptografada com sucesso!")
    print_sucesso("A mensagem criptografada está armazenada no arquivo 'enviar/mensagem_criptografada.enc'")
    salvar_arquivo("particular/mensagem_original.txt", mensagem)
    salvar_arquivo("enviar/mensagem_criptografada.enc", mensagem_criptografada)

    print("\nAssinando mensagem...")
    minha_chave_privada = ler_arquivo("particular/minha_chave_privada.pem")
    assinatura = assinar_mensagem(mensagem, minha_chave_privada)
    salvar_arquivo("enviar/assinatura.sig", assinatura)
    print_sucesso("Assinatura gerada sucesso!")
    print_sucesso("A assinatura está armazenada no arquivo 'enviar/assinatura.sig'")


def descriptografar():
    minha_chave_privada_existe = arquivo_existe("particular/minha_chave_privada.pem")
    mensagem_criptografada_existe = arquivo_existe("recebido/mensagem_criptografada.enc")

    if not mensagem_criptografada_existe:
        print_erro("Mensagem criptografada não encontrada. Peça ao seu parceiro para enviar a mensagem criptografada.")
        print_erro("Coloque a mensagem criptografada recebida em 'recebido/mensagem_criptografada.enc'")
        return

    if not minha_chave_privada_existe:
        print_erro("Chave privada não encontrada. Gere suas chaves primeiro.")
        return

    minha_chave_privada = ler_arquivo("particular/minha_chave_privada.pem")
    mensagem_criptografada = ler_arquivo("recebido/mensagem_criptografada.enc")
    mensagem_descriptografada = descriptografar_mensagem(mensagem_criptografada, minha_chave_privada)

    if mensagem_descriptografada is None:
        print_erro("Erro ao descriptografar a mensagem. Verifique se a chave privada está correta.")
        return

    print("Descriptografando mensagem...")
    print_sucesso("Mensagem descriptografada com sucesso")
    print_sucesso("Ela ficará armazenada no arquivo 'recebido/mensagem_descriptografada.txt'")
    print_sucesso(f"Mensagem descriptografada: {F.YELLOW}{mensagem_descriptografada}")
    salvar_arquivo("recebido/mensagem_descriptografada.txt", mensagem_descriptografada)

    print("\nVerificando assinatura digital da mensagem...")
    verif_assinatura(mensagem_descriptografada)


def verif_assinatura(mensagem_descriptografada: str):
    assinatura_existe = arquivo_existe("recebido/assinatura.sig")
    chave_publica_existe = arquivo_existe("recebido/chave_publica.pem")

    if not assinatura_existe:
        print_erro("Assinatura não encontrada. Peça ao seu parceiro para enviar a assinatura.")
        print_erro("Coloque a assinatura recebida em 'recebido/assinatura.sig'")
        return

    if not chave_publica_existe:
        print_erro("Chave pública não encontrada. Peça ao seu parceiro para enviar a chave pública dele.")
        print_erro("Coloque a chave pública recebida em 'recebido/chave_publica.pem'")
        return

    assinatura = ler_arquivo("recebido/assinatura.sig")
    chave_publica = ler_arquivo("recebido/chave_publica.pem")
    assinatura_valida = verificar_assinatura(mensagem_descriptografada, assinatura, chave_publica)

    if assinatura_valida:
        print_sucesso("Assinatura verificada com sucesso!")
    else:
        print_erro("Assinatura inválida! A mensagem pode ter sido alterada ou a chave pública está incorreta.")
