# For 
# No código ao lado percorremos a lista nomes e imprimimos cada elemento.
# a variável definida na linha 1 é uma lista inicializada com uma sequencia de valores do tipo string.
# a instrução for percorre todos esses elementos, um por vez, e em cada caso, atribui o valor do item á variável n, que é impressa em seguida.
# o resultado entao é  a impressão de todos os nomes contidos na lista.




nomes=["ana","bia","Broetto"]
for  n in nomes:
    print(n) # se for uma lista ele pega 1 por vez.
    # se for uma string, ele pega um caracter por vez.
    # ele imprime isso.
    #ana
 #bia
 #Broetto
##❁——————————❁❁——————————❁❁——————————❁❁——————————❁❁——————————❁❁——————————❁❁——————————❁
aluno=" ala"
for a in aluno:
    print(a)
    #ele imprime isso.
    #a
    #l
    #a
  #❁——————————❁❁——————————❁❁——————————❁❁——————————❁❁——————————❁❁——————————❁vv❁——————————❁❁——————————❁❁——————————❁

  # com a instrução break podewmos parar o loop antes que ele tenha percorrido todos os itens.

nomes=["maria","ana","fulano","margarida"]
for n in nomes:
 print(n)
 if n == "ana":# ele vai imprimir isso. maria
# ana
        break
 
# ❁——————————❁❁——————————❁❁——————————❁❁——————————❁❁——————————❁

# com a instrução continue podemos parar a iteração atual do loop e continuar com a proxima.

momes=["maria"," joaquim"," cesar"]
for n in nomes:
    continue
print(n)

# no exemplo acima quando a interação encontrar joão, o algoritmo irá pular os passos abaixo( ou seja os nomes) e seguir para a próxima interação.
# é assim que ele imprima.

# a função range() percorre um conjunto de código um determinado numero de vezes.
# a função range() retorna uma sequencia de numeros, começando em 0 por padrao e incrementos em 1(por padrao), e termina em um numeros especificado.
# o valor dentro de um parametro pode ser uma variavel.

for c in range(6):
    print(c)
# ele vai imprimir assim
 #0
#1
#2
#3
#4
#5

for b in range(5,7):# ele vai imprimir assim 5
#6
    print(b)

#o padra da função range é incrementar a sequencia em 1, no entanto é possivel especificar o valor do incremento adicionando um 3 parametro.
#range(2,10,7)
#inicio/fim/incremento(que ele pula)
for n in range(100,0,-1):
    print(n)

 # PARA COLOCAR EM FORMA DECRESCENTE.
 # for n in range(100,0,-1)
    #print(n)

    ################################################

# um loop aninhado é um loop dentro de um loop
# o loop interno sera executado uma vez para cada iteração do loop externo.
for i in range(5):
    for j in range(6):
        print(i,j)
# ele imprime isso
'''0 0
#0 1
#0 2 
#0 3
#0 4
#0 5
#1 0
#1 1
1 2
1 3
1 4
1 5
2 0
2 1
2 2
2 3
2 4
2 5
3 0
3 1
3 2
3 3
3 4
3 5
4 0
4 1
4 2
4 3
4 4
4 5'''

##########################################################3

#

# desenvolva uma calculadora de multiplicação com o for aninhado, não esqueça de seguir o padrão de impressão.

for i in range(2):
    for j in range(11):
        print(i,"x",j,"= ")