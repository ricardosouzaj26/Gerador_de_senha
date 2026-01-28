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

def main():
    while True:
        tamanho_senha = input("Insira a quantidade de dígitos desejada na senha: ")

        if not tamanho_senha.isdigit():
            print("Digite apenas números.")
            continue

        tamanho_senha = int(tamanho_senha)
        if tamanho_senha < 6:
            print("Use pelo menos 6 caracteres.")
            continue

        senha = gerador_senha(tamanho_senha)
        print(f"\nSenha gerada:\n{senha}")
        break

if __name__ == "__main__":
    main()
