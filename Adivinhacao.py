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
print("Suas tentativas: ", total_tentativas)

# Loop do jogo
for rodada in range(1, total_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_tentativas))

    chute_str = input("Digite o seu numero: ")
    chute = int(chute_str)

    if(chute < 1 or chute > 100):
        print("O número deve ser entre 1 e 100")
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print("É isso meno você é foda! ")
        break
    else:
        if(maior):
            print("Diminuii")
        elif(menor):
            print("Aumenta o bagulho")
        # rodada = rodada + 1  <- No 'for' do Python, isso não é necessário, mas mantive a lógica

print(f"O número era: {numero_secreto}")
print("Boa meno tenta de novo se tu é bem home")