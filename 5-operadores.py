num1 = int (input("Digite o primeiro número: \n"))
num2 = int (input("Digite o segundo número: \n"))

#Aritiméticos
sum = num1 + num2
sub = num1 - num2
mult = num1 * num2
div = num1 / num2
mod = num1 % num2  #Resto da divisão
exp = num1 ** num2 #Exponenciação


print(f"A soma de {num1} e {num2} é: {sum}\n")
       
print(f"A potência do número {num1} por {num2} é: {exp}")

#------------------------------------------------------------

#Comparação
bigger = num1 > num2  #Maior e sempre retorna se é verdadeiro ou falso

smaller = num1 < num2 #Menor e sempre retorna se é verdadeiro ou falso

equal = num1 == num2 #Igual e sempre retorna se é verdadeiro ou falso

different = num1 != num2 #Diferente e sempre retorna se é verdadeiro ou falso

begger_equal = num1 >= num2 #Maior ou igual e sempre retorna se é verdadeiro ou falso

smaller_equal = num1 <= num2 #Menor ou igual e sempre retorna se é verdadeiro ou falso



print(f"Ele é maior? {bigger}\n")

print(f"Ele é menor? {smaller}\n")

print(f"Ele é igual? {equal}\n")

print (f"O número 1: {num1}, é maior ou igual ao número 2 {num2}? {begger_equal}\n")


#------------------------------------------------------------


#Atribuição

num1 += num2 #num1 = num1 + num2
num1 -= num2 #num1 = num1 - num2
num1 *= num2 #num1 = num1 * num2
num1 /= num2 #num1 = num1 / num2