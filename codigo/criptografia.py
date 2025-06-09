import rsa
import base64


def gerar_chaves() -> tuple[str, str]:
    chave_publica, chave_privada = rsa.newkeys(512)
    chave_publica_pem = chave_publica.save_pkcs1().decode()
    chave_privada_pem = chave_privada.save_pkcs1().decode()
    return chave_publica_pem, chave_privada_pem


def criptografar_mensagem(mensagem: str, chave_publica_pem: str) -> str:
    chave_publica = rsa.PublicKey.load_pkcs1(chave_publica_pem)
    mensagem_cripto = rsa.encrypt(mensagem.encode(), chave_publica)
    mensagem_cripto_base64 = base64.b64encode(mensagem_cripto).decode()
    return mensagem_cripto_base64


def assinar_mensagem(mensagem: str, chave_privada_pem: str) -> str:
    chave_privada = rsa.PrivateKey.load_pkcs1(chave_privada_pem)
    hash = rsa.compute_hash(mensagem.encode(), "SHA-256")
    assinatura = rsa.sign_hash(hash, chave_privada, "SHA-256")
    assinatura_base64 = base64.b64encode(assinatura).decode()
    return assinatura_base64


def descriptografar_mensagem(mensagem_criptografada_base64: str, chave_privada_pem: str) -> str | None:
    chave_privada = rsa.PrivateKey.load_pkcs1(chave_privada_pem)
    mensagem_recebida = base64.b64decode(mensagem_criptografada_base64)

    try:
        return rsa.decrypt(mensagem_recebida, chave_privada).decode()
    except rsa.DecryptionError:
        return None


def verificar_assinatura(mensagem: str, assinatura_base64: str, chave_publica_pem: str) -> bool:
    chave_publica = rsa.PublicKey.load_pkcs1(chave_publica_pem)
    assinatura = base64.b64decode(assinatura_base64)

    try:
        rsa.verify(mensagem.encode(), assinatura, chave_publica)
        return True
    except rsa.VerificationError:
        return False
