# Lista no python
#python - valores em uma lista.

# existem varias maneiras de se criar uma nova lista, a maneira mais simples é envolver os elementos da lista popr colchetes[]

a=[10,23,78]
b=["bia",67,"ana",90]
print(a)
print(type(a))

print(b)
print(type(b))

################################################
# a lista a seguir contem um string, u float, uj inteiro, e uma outra lista.
# uma lista em uma outyra lista é dita aninhada(nested) e a lista mais interna é chamada frequentemente de sublista(sublist).
#  finalmente, existe uma lista especial, que não contem elemento algum. ela é chamada de lista vazia e é denotada por []

lista=["oi"],45,7.8,[10,78]
print(lista)

###########################################333

# python- comprimeto de uma lista.

#da mesma forma que ocorre com strings a função len retorna o comprimeto de uma lista( o numero de le,mentos na lista.)
# entretanto como listas podem conter itens que sao listas e importante notar que len somente retorna o comprimeto da list mais externa. 
# em outras palavras, sublistas de uma lista são consideradas como sendo um elemento simples quando contamos o comprimento da lista.

list=["a",2,["a",3]]
print(len(list))

###########################################################

# python- acessando os elementos.

# a sintaxe para acessar um elemento de uma lista é a mesma usada para acessar um caracter de um string.

# e utilizado o operador de indexação([]-nao confundir com a lista vazia)
a=(" Bia")
print(a[3])
#################################################################3

# python-comprimeto de uma lista
#ele pega um elemnto que eu quero
uma_lista=[3,67,"gato",[56,57,"cachorro"],[],3.67,False]
print(uma_lista[3][1])

################################################################

#python- Pertinência em uma lista.

#in e not são operadores booleanos ou logicos que testam a pertinencia(membership) em uma sequencia.
# esses operadores funcionam com strings e eles tambem funcinam aqui.

animais=[" cachorro"," borboleta"]
print("gato"in animais)

print(" arara" not in animais)## not é não em portugues

##########################################################3

#python- pertinencias em uma lista

# assim como com strings o operador+ concatena(junta) as listas.
# analogamente , o operador* repete os itens em uma lista um dado do numero de vezes.

frutas=["maca","laranja"," banana"]
print([1,2]+[3,4])

print(frutas+[6,7,8,9])

print([]*4)
print([1,2,["ola","adeus"]]*2)

###############################################

#python- max,min,sum

#o python oferece ainda as funcoes min(), max(), e sum(),
# atraves das quais é possivel encontrar respectivamente, o menor valor, o maior valor ou ainda realizar a soma de todos os elementos da lista.

a=[1,2,3,4,5,6,7,8,9]
print(a)
print(max(a))
print(min(a))
print(sum(a))

a=[1,2,3,4,5,6,7,8,9]
print(sum(a)/len(a))# importante!

####################################################################

# Python- fatias de listas.

# a operação de fatiar (slice) que e vista tambem com strings pode der aplicada sobre listas.
# lembre que o primeiro indice indica o ponto do inicio da fatia e o segundo indice e um depois do final da fatia(o elemento com esse indice nao faz parte da fatia)

uma_lista= ["a","b","c","d","e","f"]
print(uma_lista[1:3])
print(uma_lista[:4])
print(uma_lista[3:])
print(uma_lista[:])
print(uma_lista[0:6])

######################################

#python listas mutaveis(ela é alteravel, pode ser alterada)

# diferentemente de strings, listas são mutaveis(mutable)
# isto significa que podemos alterar um item em uma lista acessando-o diretamente como parte do comando de atribuição.
#usando o operador e indexação(colchetes) a esquerda de um comendo de atribuicao podemos atualizar um dos itens de uma lista.

frutas= ["banana","maca","cereja"]

frutas[0]="pera"
frutas[-1]="goiaba"
print(frutas)## ele imprime isso->['pera', 'maca', 'goiaba'] 
## da pra trocar e "mudar de lugar" os objetos que nesse casso são as frutas.

lista=[" flor","azul",["1","casa"]]
lista[2][1]=" escola"
print(lista)# substituiu casa por escola.
#[' flor', 'azul', ['1', ' casa']]
#[' flor', 'azul', ['1', ' escola']]

#############################################################

#python listas mutáveis.

# combinando uma atribuição com o operador de fatiamento

uma_lista=["a","b","c","d","e","f"]
uma_lista[1:3]=["5","0"] ## ele vai trocar a letra b pelo numero 5, e a letra c pelo numero 0 . ['a', '5', '0', 'd', 'e', 'f'] 
# VAI FICAR ASSIM ->['a', '5', '0', 'd', 'e', 'f']
print(uma_lista)

##############################################
# 
uma_lista=["a","b","c","d","e","f"]
print(uma_lista)
print(len(uma_lista))

uma_lista[1:3]=[] # ele exclui os elementos que eu selecionar!
print(uma_lista)
print(len(uma_lista))
# ele mostra quantos caracteres tem na lista inicial, e depois mostra quantos que ficou na lista final.

#############################################################
# podemos inserir elementos em uma lista espremendo-os em uma fatia vazia na posição 
# colocar o intervalo onde o elemento sera inserido.

uma_lista=["a","b","c"]
uma_lista[1:1]=["r","8"]
print(uma_lista)

uma_lista[4:4]=["6"]
print(uma_lista)## ele adiciona o elemento na lista.

###########################################33
#python - remoção de listas
#del(deletar)

a= [" Um","dois","tres"] # ele deleta [' Um', 'tres']
del a[1]
print(a)

lista=["a","b","c","d","e","f"]
del lista[1:5] # ele deleta ['a', 'f']
print(lista)

############################################
#python- operador.(ponto)

# o operador ponto tambem pode ser usado para acessar metodos nativos(built-in) de objetos que são listas.append 
# é um metodo de listas que insere o argumento passado para ele no final da lista.

a=[81,45,78]
a.append(5)
print(a)

###########################################
# python- operador.(ponto)

#sort e um metodo de listas que ordena os valores contidos em uma lista
# reverse e um metodo de listas que inverte a ordem da lista mas nao a ordena.
# lista.sort(reverse=true)ordena os valores de ordem reversa.

a=[56,89,67,8]# ele deixa em ordem crescente
a.sort()
print(a)

a=[3,6,7,8]
a.reverse()
print(a)# ele reverte a ordem que foi colocada [8, 7, 6, 3]

a=[3,6,7,8]
a.sort(reverse=True)
print(a)


##########################################################3
# INdex

# o index é um metodo de listas que retorna a posição do objeto na primeira vez que ele aparece.
###0,1,2,3,4,5,6,7,8,-> posições dos numeros
a=[1,2,3,4,5,6,7,8,9] # ele  mostra a posição que esta o numero.
print(a.index(6))
# ele vai imprimir isso aui->5

##############################################
# INSERT

# insert e um metodo de listas que insere o valor na posição desejada. informa a posição e posteriormente o valor.
# insert(indice,elemento)

a=[1,2,3,4,5]
a.insert(2,100) ## ele adiciona o elemento na posição desejada.[1, 2, 100, 3, 4, 5]
print(a)

#####################################################################3
# Count

# count e um metodo de listas que conta quantas vezes o valor informado aparece na lista.
a=[1,2,3,4,5,6,7]
print(a.count(4))

# ele conta quantas vezes aparece o valor informado. ele imprime isso->1

###############################################################
# pop

# existem duas maneiras de usar o metodo pop. a primeira sem parametros, remove e retorna o ultimo da lista.
# se for dado um argumento para a posicao, pop remove o item da posição. de qualquer maneira a lista e alterada.
# se colocar () parenteses vazios ele remove o ultimo item da lista.

a=[1,2,3,4]
a.pop()
print(a)

a.pop(0)
print(a)

###############################################333
#