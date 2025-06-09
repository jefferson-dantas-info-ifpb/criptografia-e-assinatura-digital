# Criptografia e Assinatura Digital

**Alunos:**\
José Jefferson Dantas Araújo\
Marcos Paulo Santos Lira

## Gerar suas chaves pública e privada
- `chave_publica_b.pem`
- `chave_privada_b.pem`

```sh
python gerar_chaves.py
```

## Criptografar uma mensagem
1. Coloque a chave pública de A na pasta `chaves` com o nome `chave_publica_a.pem`

2. Execute
```sh
python criptografar_mensagem.py
```

3. O resultado ficará em `mensagens/mensagem_crypto.txt`

## Descriptografar uma mensagem
```sh
python descriptografar_mensagem.py
```
