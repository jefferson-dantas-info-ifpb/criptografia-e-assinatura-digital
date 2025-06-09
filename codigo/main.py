from acoes import gerar_chaves_e_guardar, criptografar, descriptografar, verif_assinatura


def main():
    opcao = input(
        """
Bem-vindo ao sistema de criptografia!
Escolha uma opção:

  1. Gerar chaves e guardar
  2. Criptografar mensagem
  3. Descriptografar mensagem

Digite o número da opção desejada:
"""
    )

    if opcao == "1":
        gerar_chaves_e_guardar()
    elif opcao == "2":
        criptografar()
    elif opcao == "3":
        descriptografar()


if __name__ == "__main__":
    while True:
        main()
        input("Pressione Enter para continuar...")
