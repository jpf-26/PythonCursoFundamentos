movie1 = "Top Gun"
movie2 = "top gun"

print(movie1 == movie2)  #Falso e o python é case sensitive


descricaoFilme = """
            O filme Top Gun é um filme de ação militar
          que foi lançado em 1986 e é estrelado por Tom Cruise
        e Kelly McGillis. O filme foi dirigido por Tony Scott e
        produzido por Don Simpson e Jerry Bruckheimer.    
"""


"""
Apesar de utilizar 3 àspas para comentários, consegue utiliza-las dessa forma acima para por exemplo descrição de um filme
"""

print (movie1)


#Multiplicando strings
line = "="

print (line * 63)

print (descricaoFilme)


#Procurando uma palavra dentro de uma string

print ("top" in movie2) 