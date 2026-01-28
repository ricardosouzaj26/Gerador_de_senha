#password_generator

import random
import string

def gerador_senha(s):
    numerico = string.digits
    letra = string.ascii_letters
    especial = string.punctuation
    alternativas = numerico + letra + especial
    senha = ""
    for i in range(0, s):
        digito = random.choice(alternativas)
        senha += digito
    return senha



tamanho_senha = input("Insira a quantide de dígitos desejada na senha: ")
if tamanho_senha.isdigit():
    tamanho_senha = int(tamanho_senha)
    senha = gerador_senha(tamanho_senha)
else:
    print("Reinicie o programa e insira um valor numérico.")
    quit()

print(f"Senha gerada:\n{senha}")