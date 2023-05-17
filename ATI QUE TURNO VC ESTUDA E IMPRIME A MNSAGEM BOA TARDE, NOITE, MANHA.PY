 # faça um programa que pergunte em que turno você estuda. Peça para digitar M-matutino, V- vespertino ou N- Noturno. imprima a mensagEM " bOMDIA, BOA NIOTE , BOA TRADE OU VALOR INVALIDO."

turno= input(" Olá, digite M para matutino, V para vespertino ou N para noturno:")

if turno==("m" or " M"):
    print( " Buenos Dias")

elif turno==("v" or "V"):
 print(" Buenas tardes")    

elif turno==("n" or " N"):
   print(" Buenas Noches") 

else:
   print(" Valor inválido!")