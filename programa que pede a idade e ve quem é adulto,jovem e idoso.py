# faca um programa que peça para n pessoas,
# a sua idade, ao final o programa devera verificar se a média
# de idade da turma varia entre o e 25, 26 e 60 e maior que 60; e entao dizer se a turma é jovem, adulta ou idosa, conforme a média
# calculada.
# imprimir a quantidade de jovem, adulto e idoso.

count=0
while True:
    op=input(" Digite 1 para entrar, e x para sair!")
    if op=="x" and "X":
        print(" Saindo...")
        print(" Bay")
        break
    elif  op=="1":
        print(" Bem vindo!")
        id=int(input(" Digite a sua idade:"))
        count=count+1
    
        media=(count+id)/2

    if op=="x" and "X":
        print(" Saindo...")
        print(" Bay")
        break

    if media >0 and media <25:
        print(" Turma jovem") 
       
    elif media >26 and media <60:
        print(" Turma adulta")
      
    elif media >=60:
        print(" Turma idosa.")    
        
    if op=="x" and "X":

    
    

        print(" ")
        
   
 
    


    
