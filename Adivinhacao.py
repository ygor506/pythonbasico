import random



#cores no terminal PY
vermelho = "/033[31m]"
verde = "/033[32m]"
amarelo ="/033[33m]"
azul ="/033[34m]"
RESET = "/033[35m]"

def escolher_nivel():
   print("/nEscolha o nivel: ")
   print("1 -- facil (10 tentativas)")
   print("2 -- medio (5 tentativas)")
   print("3 -- dificil (3 tentativas)")

   while True:
      nivel_str = input("Digite apenas números (1, 2, 3): ")
      if not nivel_str.isdigit():
         print(vermelho+"Digite apenas Números! "+ RESET)
         continue
      nivel_str = int(nivel_str)
      if nivel == 1:
         return 10
      elif nivel == 2:
         return 5
      elif nivel == 3:
         return 3
      else:
         print(amarelo+"escolha apenas 1, 2 ou 3"+RESET)


def jogar():
   
   print(azul+'*********************************'+RESET)
print(azul+'*********Jogo adivinhação********'+RESET)
print(azul+'*********************************'+RESET)


total_tentativas = escolher_nivel()
numero_secreto = random.randrange(1,31)
pontos = 100
historico = []


for rodada in range(1, total_tentativas + 1):
  print("tentativa {rodada} de {total_tentativas}".format(rodada,total_tentativas))
  chute_str = input("Digite um número 1 entre 100: "+RESET)
 
  chute = int(chute_str)

  print("Seu numero é" == chute_str)
  

  if(chute < 1 or chute > 30):
     print("Você deve digitar um numero entre 1 e 30! ") 
     continue
  

  acertou = chute == numero_secreto
  maior = chute > numero_secreto
  menor = chute < numero_secreto

  if(acertou):
    print("Você Acertou!! ")
    break
  else:
for rodada in range(1, total_tentativas + 1):
  print("tentativa {} de {}".format(rodada,total_tentativas))

  chute_str = input("Digite o seu número: ")
  print("Seu numero é" == chute_str)
  chute = int(chute_str)

  if(chute < 1 or chute > 30):
     print("Você deve digitar um numero entre 1 e 30! ") 
     continue
  

  acertou = chute == numero_secreto
  maior = chute > numero_secreto
  menor = chute < numero_secreto

  if(acertou):
    print("Você Acertou!! ")
    break
  else:
    if(maior):
        print("O seu chute foi maior que o numero secreto")
    elif(menor):
        print("O seu chute foi menor que o numero secreto")
    if(maior):
        print("O seu chute foi maior que o numero secreto")
    elif(menor):
        print("O seu chute foi menor que o numero secreto")
   
   











print('*********************************')
print('*********Jogo adivinhação********')
print('*********************************')
 
numero_secreto = random.randrange(1,46)
total_tentativas = 5
rodada = 1

dificuldade_facil = 1
dificuldade_media = 2
dificuldade_dificil = 3

print("dificuldade escolhida", escolha)


print("Fim de jogo!")
