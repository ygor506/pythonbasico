while True:
     try:
        idade = int(input("Digite sua idade"))
        if idade <=10:
           print("A idade deve ser maior que 10.")
        else:
           break
     except ValueError:
       print("Digite apenas numeros inteiros.")

print("Idade cadastrada: ", idade)

    