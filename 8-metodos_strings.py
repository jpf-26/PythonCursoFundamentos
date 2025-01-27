movie1 = "Top Gun"
descricaoFilme = """
            O filme Top Gun, é um filme de ação militar
          que foi lançado em 1986 e é estrelado por Tom Cruise
        e Kelly McGillis, O filme foi dirigido por Tony Scott e
        produzido por Don Simpson e Jerry Bruckheimer.    
"""

print (movie1.upper()) #Tudo em maiúsculo
print (movie1.lower()) #Tudo em minúsculo
print (movie1.capitalize()) #Primeira letra em maiúsculo
print (movie1.title()) #Primeira letra de cada palavra em maiúsculo
print (movie1.center(20, "-")) #Centraliza a string e preenche com o caractere informado
print(movie1.find("u")) #Encontra a posição da primeira ocorrência
print (movie1.replace("Top", "Matrix")) #Substitui uma palavra por outra
print (descricaoFilme.split(",")) 