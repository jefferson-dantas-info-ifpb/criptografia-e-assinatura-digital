def arquivo_existe(nome: str) -> bool:
    try:
        with open(nome, "r"):
            return True
    except FileNotFoundError:
        return False


def salvar_arquivo(nome: str, conteudo: str):
    with open(nome, "w") as f:
        f.write(conteudo)


def ler_arquivo(nome: str) -> str:
    with open(nome, "r") as f:
        return f.read()
