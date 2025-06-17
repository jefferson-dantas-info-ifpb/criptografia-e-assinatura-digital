from utils import arquivo_existe, ler_arquivo, print_aviso, print_erro, print_sucesso, salvar_arquivo
from colorama import Fore as F
from criptografia import (
    assinar_mensagem,
    descriptografar_mensagem,
    gerar_chaves,
    criptografar_mensagem,
    verificar_assinatura,
)

NOSSA_CHAVE_PUBLICA_ISAIAS_TIAGO = "isaias_tiago/chave_publica_a.pem"
NOSSA_CHAVE_PRIVADA_ISAIAS_TIAGO = "isaias_tiago/chave_privada_a.pem"
CHAVE_PUBLICA_ISAIAS_TIAGO = "isaias_tiago/chave_publica_b.pem"
MENSAGEM_ENVIAR_ORIGINAL = "isaias_tiago/mensagem.txt"
MENSAGEM_ENVIAR_CRIPTOGRAFADA = "isaias_tiago/mensagem_cripto.txt"
ASSINATURA_ENVIAR = "isaias_tiago/assinatura.bin"

NOSSA_CHAVE_PUBLICA_ERIK_LUCAS = "erik_lucas/chave_publica_b.pem"
NOSSA_CHAVE_PRIVADA_ERIK_LUCAS = "erik_lucas/chave_privada_b.pem"
CHAVE_PUBLICA_ERIK_LUCAS = "erik_lucas/chave_publica_a.pem"
MENSAGEM_RECEBIDA_CRIPTOGRAFADA = "erik_lucas/mensagem_cripto.txt"
MENSAGEM_RECEBIDA_DESCRIPTOGRAFADA = "erik_lucas/mensagem_recebida.txt"
ASSINATURA_RECEBIDA = "erik_lucas/assinatura.bin"
RESULTADO_ASSINATURA = "erik_lucas/assinatura_verificada.txt"


def gerar_chaves_e_guardar():
    chave_existente = verificar_chave_existente()
    if chave_existente:
        return

    print("Gerando chaves...")
    chave_publica_pem, chave_privada_pem = gerar_chaves()
    salvar_arquivo(NOSSA_CHAVE_PUBLICA_ISAIAS_TIAGO, chave_publica_pem)
    salvar_arquivo(NOSSA_CHAVE_PRIVADA_ISAIAS_TIAGO, chave_privada_pem)
    salvar_arquivo(NOSSA_CHAVE_PUBLICA_ERIK_LUCAS, chave_publica_pem)
    salvar_arquivo(NOSSA_CHAVE_PRIVADA_ERIK_LUCAS, chave_privada_pem)
    print_sucesso("Chaves geradas com sucesso!")


def verificar_chave_existente():
    existe_publica_it = arquivo_existe(NOSSA_CHAVE_PUBLICA_ISAIAS_TIAGO)
    existe_privada_it = arquivo_existe(NOSSA_CHAVE_PRIVADA_ISAIAS_TIAGO)
    existe_publica_el = arquivo_existe(NOSSA_CHAVE_PUBLICA_ERIK_LUCAS)
    existe_privada_el = arquivo_existe(NOSSA_CHAVE_PRIVADA_ERIK_LUCAS)
    if not existe_publica_it and not existe_privada_it and not existe_publica_el and not existe_privada_el:
        return False

    resposta = input("Já existem chaves geradas. Deseja gerar novas chaves? (s/N): ")
    if resposta.strip().lower() == "s":
        return False
    else:
        print_aviso("Cancelado")
        return True


def criptografar():
    chave_publica_existe = arquivo_existe(CHAVE_PUBLICA_ISAIAS_TIAGO)
    nossa_chave_privada_existe = arquivo_existe(NOSSA_CHAVE_PRIVADA_ISAIAS_TIAGO)

    if not chave_publica_existe:
        print_erro("Chave pública não encontrada. Peça ao seu parceiro para enviar a chave pública dele.")
        print_erro(f"Coloque a chave pública recebida em '{CHAVE_PUBLICA_ISAIAS_TIAGO}'")
        return

    if not nossa_chave_privada_existe:
        print_erro("Chave privada não encontrada. Gere suas chaves primeiro.")
        return

    chave_publica = ler_arquivo(CHAVE_PUBLICA_ISAIAS_TIAGO)
    mensagem = input("Digite a mensagem a ser criptografada: ")
    print("\nCriptografando mensagem...")
    mensagem_criptografada = criptografar_mensagem(mensagem, chave_publica)
    print_sucesso("Mensagem criptografada com sucesso!")
    print_sucesso(f"A mensagem criptografada está armazenada no arquivo '{MENSAGEM_ENVIAR_CRIPTOGRAFADA}")
    salvar_arquivo(MENSAGEM_ENVIAR_CRIPTOGRAFADA, mensagem_criptografada)
    salvar_arquivo(MENSAGEM_ENVIAR_ORIGINAL, mensagem)

    print("\nAssinando mensagem...")
    nossa_chave_privada = ler_arquivo(NOSSA_CHAVE_PRIVADA_ISAIAS_TIAGO)
    assinatura = assinar_mensagem(mensagem, nossa_chave_privada)
    salvar_arquivo(ASSINATURA_ENVIAR, assinatura)
    print_sucesso("Assinatura gerada sucesso!")
    print_sucesso(f"A assinatura está armazenada no arquivo '{ASSINATURA_ENVIAR}'")


def descriptografar():
    nossa_chave_privada_existe = arquivo_existe(NOSSA_CHAVE_PRIVADA_ERIK_LUCAS)
    mensagem_criptografada_existe = arquivo_existe(MENSAGEM_RECEBIDA_CRIPTOGRAFADA)

    if not mensagem_criptografada_existe:
        print_erro("Mensagem criptografada não encontrada. Peça ao seu parceiro para enviar a mensagem criptografada.")
        print_erro(f"Coloque a mensagem criptografada recebida em '{MENSAGEM_RECEBIDA_CRIPTOGRAFADA}'")
        return

    if not nossa_chave_privada_existe:
        print_erro("Chave privada não encontrada. Gere suas chaves primeiro.")
        return

    nossa_chave_privada = ler_arquivo(NOSSA_CHAVE_PRIVADA_ERIK_LUCAS)
    mensagem_criptografada = ler_arquivo(MENSAGEM_RECEBIDA_CRIPTOGRAFADA)
    mensagem_descriptografada = descriptografar_mensagem(mensagem_criptografada, nossa_chave_privada)

    if mensagem_descriptografada is None:
        print_erro("Erro ao descriptografar a mensagem. Verifique se a chave privada está correta.")
        return

    print("Descriptografando mensagem...")
    print_sucesso("Mensagem descriptografada com sucesso")
    print_sucesso(f"Ela ficará armazenada no arquivo '{MENSAGEM_RECEBIDA_DESCRIPTOGRAFADA}'")
    print_sucesso(f"Mensagem descriptografada: {F.YELLOW}{mensagem_descriptografada}")
    salvar_arquivo(MENSAGEM_RECEBIDA_DESCRIPTOGRAFADA, mensagem_descriptografada)

    print("\nVerificando assinatura digital da mensagem...")
    verif_assinatura(mensagem_descriptografada)


def verif_assinatura(mensagem_descriptografada: str):
    assinatura_existe = arquivo_existe(ASSINATURA_RECEBIDA)
    chave_publica_existe = arquivo_existe(CHAVE_PUBLICA_ERIK_LUCAS)

    if not assinatura_existe:
        print_erro("Assinatura não encontrada. Peça ao seu parceiro para enviar a assinatura.")
        print_erro(f"Coloque a assinatura recebida em '{ASSINATURA_RECEBIDA}'")
        return

    if not chave_publica_existe:
        print_erro("Chave pública não encontrada. Peça ao seu parceiro para enviar a chave pública dele.")
        print_erro(f"Coloque a chave pública recebida em '{CHAVE_PUBLICA_ERIK_LUCAS}'")
        return

    assinatura = ler_arquivo(ASSINATURA_RECEBIDA)
    chave_publica = ler_arquivo(CHAVE_PUBLICA_ERIK_LUCAS)
    assinatura_valida = verificar_assinatura(mensagem_descriptografada, assinatura, chave_publica)

    if assinatura_valida:
        print_sucesso("Assinatura verificada com sucesso!")
        salvar_arquivo(RESULTADO_ASSINATURA, "Assinatura verificada com sucesso!")
    else:
        print_erro("Assinatura inválida! A mensagem pode ter sido alterada ou a chave pública está incorreta.")
        salvar_arquivo(
            RESULTADO_ASSINATURA,
            "Assinatura inválida! A mensagem pode ter sido alterada ou a chave pública está incorreta.",
        )
