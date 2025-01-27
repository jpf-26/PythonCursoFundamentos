nomeFilme = "Top Gun"

#string [Ínicio: Fim] - índice começa na posição 0 e vai até o fim e faz -1

#1 - Buscar toda a string a partir da primeira posição 
print (nomeFilme[0:])

#2-Buscar toda a string até a posição final lembrando que se colocar 6 ele faz -1, por isso colocar o 7 para pegar a string inteira
print (nomeFilme[:7])

#3- Buscar toda a string a partir da posição 3, lembrando que sempre diminuir ou colocar uma posição a mais por causa do -1
print (nomeFilme[2:])


#string [Ínicio: Fim: Passo]  - Passo determina o incremento e por padrão ele é 1
#4- Buscar toda a string de 2 em 2 caracteres
print (nomeFilme[::2])


#5 Buscar toda a string nas posições ímpares
print (nomeFilme[1::2])


#6- Buscar toda a string de trás para frente
print (nomeFilme[::-1])




