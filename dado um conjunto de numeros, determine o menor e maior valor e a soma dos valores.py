# faça um programa que, dado um conjunto de N, números, determine
# o menor valor, o maior valor e a soma dos valores. de todos os valores que entrarem.
# para convereter para valores inteiros num=int(num)

lista=[]
while True:
       a=(input(" Digite o valor:"))
       if a=="x":
          break
       a=int(a)
       lista.append(a)

if a=="x":
       print("Saindo....")
       if len(lista)!=0:
          print(min(lista))  
          print(max(lista))   
          print(sum(lista))    
               


  #num.append[soma]

