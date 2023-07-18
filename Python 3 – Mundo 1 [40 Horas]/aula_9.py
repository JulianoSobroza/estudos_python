# CADEIAS DE STRING
"""
'Curso em vídeo Python' - isso é uma cadeia de caracteres ou
cadeia de textos, elas estão sempre em aspas duplas ou sim-
ples.

"""

# Fatiamento

frase = 'Curso em vídeo Python'
(frase[9]) #Vai printar somente o décimo caractere (V)
(frase[9:14]) # Vai printar de 9 a 14 (Vídeo)
(frase[9:21:2]) # vai saltando de 2 em 2
(frase[:5]) # vai do começo até o 5
(frase[9::3])


# Análise

print(len(frase)) #len = comprimento = 21 caracteres
frase.count('o') # programa vai contar quantas vezes aparece 'o' minusculo
frase.count('o',0, 13)
frase.find('deo')

# Transformação

#frase.replace('Python, Android') #substitui Python por Android
frase.upper() # método de deixar todas as letras em maiúsculo
frase.lower() # métrodo de deixar todas as letras em minúsculo
frase.capitalize() # tona somente a primeira letra maiúscula
frase.title () # torna as primeiras letras maiusculas
frase.strip () #remove os espaços inúneis no inicio e no final da frase
frase.rstrip()
frase.lstrip()

# Disvisão
frase.split()
print('-'.join(frase))  #adiciona traços entre as palavras



#print ("""One Monday afternoon, Mike, adopting a very unusual
#  style, wore a hoody. Nobody would ever think of wearing a 
# hoody on a very hot day. His friends also wondered why he
#  was being weird. They became a little aloof with Mike that
#  day. The next day, Mike wore a hoody again, this time of a 
# different color. This went on every day for a week and his
#  friends gradually got used to it. Finally, on the eighth 
# day, Mike wore a plain white shirt, acting like nothing had
#  been amiss for the past week. One of his friends asked him,
#  “Are you finally done with your hoody fashion?” “What hoody 
# fashion?” Mike asked. “Last week, everyday, you kept on
#  wearing a hoody.” And then Mike said, “What? I was on vaca-
# tion last week. I just got home this morning. ”""")
