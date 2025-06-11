from acoes import gerar_chaves_e_guardar, criptografar, descriptografar
from colorama import init as coloramaInit, Style as S, Fore as F
from utils import print_erro

coloramaInit(autoreset=True)


def main():
    opcao = input(
        f"""
╭──────────────────────────────────────────────╮
│ {F.MAGENTA}SISTEMA DE CRIPTOGRAFIA E ASSINATURA DIGITAL{S.RESET_ALL} │
├──────────────────────────────────────────────┤
│ {F.BLUE}Escolha uma opção:                          {S.RESET_ALL} │
│                                              │
│  {F.GREEN}1. {F.CYAN}Gerar chaves e guardar{S.RESET_ALL}                   │
│  {F.GREEN}2. {F.CYAN}Criptografar mensagem{S.RESET_ALL}                    │
│  {F.GREEN}3. {F.CYAN}Descriptografar mensagem{S.RESET_ALL}                 │
╰──────────────────────────────────────────────╯
Digite o número da opção desejada: {F.GREEN}"""
    )
    print(S.RESET_ALL)

    if opcao == "1":
        gerar_chaves_e_guardar()
    elif opcao == "2":
        criptografar()
    elif opcao == "3":
        descriptografar()
    else:
        print_erro("Opção inválida")


if __name__ == "__main__":
    try:
        while True:
            main()
            input(f"\n{F.BLUE}PRESSIONE [ENTER] PARA CONTINUAR... {S.RESET_ALL}")
    except KeyboardInterrupt:
        print(f"\n\n{F.YELLOW}Saindo...", end="")
    except Exception as err:
        print_erro(f"Ocorreu um erro: {err}")
