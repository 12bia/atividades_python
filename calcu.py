


while True:
  
  print(" Calculadora  \n1 - soma\n2 - subtração\n3 - multiplicação\n4 para divisão\n5- Volume de um cubo\n6 - Exponenciação\n7 - Raiz quadrada\n8 - área de um quadrado\n9- média de 4 números\n10- Fatorial")
  operacao= input("Selecione uma opção:")
  print("=================================================================")
 
  
  if operacao=="1":
     n1=int(input(" Digite um número:"))
     n2=int(input(" Digite um número:"))

     soma=n1+n2
     print(" A soma é de :",soma)

    

  elif operacao=="2":
     n1=int(input(" Digite um número:"))
     n2=int(input(" Digite um número:"))

     result=n1-n2
     print(" A subtração é de :",result)

  elif operacao=="3":
     n1=int(input(" Digite um número:"))
     n2=int(input(" Digite um número:"))

     result=n1*n2
     print(" A multiplicação é de :",result)

  elif operacao=="4":
     n1=int(input(" Digite um número:"))
     n2=int(input(" Digite um número:"))

     result=n1/n2
     print(" A divisão é de :",result)  

  elif operacao=="5":
     n1=float(input(" Digite a altura :"))
     n2=float(input(" Digite a largura:"))
     n3=float(input(" Digite o comprimento:"))

     result=(n1*n2)*n3
     print(" O Volume do cubo é de",result)

  elif operacao=="6":
     n1=float(input(" Digite um numero para ser a base:"))
     n2=float(input(" Digite um numero para ser o expoente:"))

     result=n1**n2
     print(" A exponenciação é de:", result)

  elif operacao=="7": 
     import math
     num = float(input("Digite um número para converter em Raiz:\n"))
     raiz = math.sqrt(num)
     print(f'\nA raiz quadrada de {num} é {raiz}\n')

  elif operacao=="8":
     lado = float(input('Digite a altura do quadrado: '))
     areaq = lado**2
     print('A área do quadrado é de ', areaq)

  elif operacao=="9": 
     n1=float(input(" digite a nota 1:")) 
     n2=float(input(" digite a nota 1:")) 
     n3=float(input(" digite a nota 1:")) 
     n4=float(input(" digite a nota 1:")) 

     result=(n1+n2+n3+n4)/4

     print(" O resultado da média é de:",result)

  elif operacao=="10":
      numero = int(input("escreva um número que deseja fatoriar: ") )

      resultado=1
      count=1

      while count <= numero:
       resultado *= count
      count += 1

      print(resultado)


     



  
  '''elif operacao=="0":
   break'''





