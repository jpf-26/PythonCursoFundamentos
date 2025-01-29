nome = input("Digite seu primeiro nome: \n")
nome2 = input("Digite seu segundo nome: \n")

print(f"Seu ultimo nome é: {nome2} e seu primeiro nome é: {nome}")

nomeContrario = (nome[::-1])

print(f"{nomeContrario}")

equal =  nome == nomeContrario

print(f"Ele é igual? {equal}\n")


