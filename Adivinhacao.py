import random

# Cores no Terminal PY
VERMELHO = "\033[31m"
VERDE = "\033[32m"
AMARELO = "\033[33m"
AZUL = "\033[34m"
RESET = "\033[0m"

print(f"{AZUL}**************************{RESET}")
print(f"{AZUL}*****Jogo adivinhação*****{RESET}")
print(f"{AZUL}**************************{RESET}")

numero_secreto = random.randrange(1, 101)
total_tentativas = 0

print("Qual dificuldade você gostaria de jogar? ")
print("(1) Fácil (2) Médio (3) Difícil ")

while True:
    try:
        dificuldade = int(input("Defina a dificuldade (1-2-3): "))

        if dificuldade == 1:
            total_tentativas = 10
            break
        elif dificuldade == 2:
            total_tentativas = 5
            break
        elif dificuldade == 3:
            total_tentativas = 3
            break
        else:
            print(f"{AMARELO}Opção inválida! Digite 1, 2 ou 3.{RESET}")
    except ValueError:
        print(f"{VERMELHO}Por favor, digite um número inteiro.{RESET}")

print(f"Você terá {total_tentativas} tentativas.")


for rodada in range(1, total_tentativas + 1):
    print(f"{AMARELO}Tentativa {rodada} de {total_tentativas}{RESET}")
    
    chute_str = input(f"{AZUL}Digite o seu número: {RESET}")
    
    try:
        chute = int(chute_str)
    except ValueError:
        print(f"{VERMELHO}Por favor, digite um número válido!{RESET}")
        continue

    if chute < 1 or chute > 100:
        print(f"{AMARELO}O número deve ser entre 1 e 100{RESET}")
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if acertou:
        print(f"{VERDE}É isso! Parabéns, você acertou!{RESET}")
        break
    else:
        if maior:
            print(f"{VERMELHO}Diminuir... tente um número menor.{RESET}")
        elif menor:
            print(f"{VERMELHO}Aumentar... tente um número maior.{RESET}")


if not acertou:
    print(f"\n{AZUL}O número secreto era: {numero_secreto}{RESET}")
    print(f"{AZUL}Boa, tenta de novo se você quiser!{RESET}")