def nota():


 while True:
     op=input(" Digite 1 para continuar ou 0 para sair:")# para continuar coloco o 1 e para sair é o 0.
     if op=="0":
         print("** Obrigada por usar o programa, volte sempre! ** ")
         break
     
     elif op=="1":
      print(" <<<<<<< Bem vindo ao ミ★ Sistema de Notas ★彡!>>>>>>") 
      # boas vindas!, SE a pessoa digitar números negativos, ou maior que 100, ele imprime "Nota inválida! Por favor digite uma nota de 0 a 100!""
     notas=float(input("<<<<<<  Por favor, digite uma nota de 0 a 100: >>>>>>>\n✎ :"))# pedir para o usuário digitar uma nota de 0 a 100.
    # Começa os elementos de condições, 
    # ou seja os testes para ver se a condição é verdadeira ou falsa.
     if notas >-1 and notas<60:# para o código pegar o número 0 e mostrar como F, tive que colocar -1 e menor que 60
            print(">>>> Nota F!")# ele imprime f de falhou.

     elif notas>=60 and notas<=62:# se a primeira  condição(o IF)for falsa, ele irá para a segunda condição que é o senão.
            print(">>>> Nota D-") #ele ira ver se nota é maior ou igual a 60 e 62, se for ele imprime nota D- que é pouco suficiente.
    
     elif notas>=63 and notas<=66:# para entrar nessa tem que colocar >="número" and <="número"
            print(">>>> Nota D")# se for esse , ele imprime o D de pouco suficiente.

     elif notas >=67 and notas<=69:# em todas as condições está >="numero" and <="numero" para que ele entre na condição.
            print(">>>> Nota D+")# ele irá imprimir D+ de pouco suficiente.

     elif notas >=70 and notas<=72:# em todas as condições está >="numero" and <="numero" para que ele entre na condição.
            print(">>>> Nota C-")# ele irá imprimir C- de pouco suficiente.

     elif notas>=73 and notas<=76:#se notas >=73 e <=76
            print(">>>> Nota C")# ele irá imprimir c de suficiente.

     elif notas >=77 and notas<=79:#se notas >=77 e notas<=79
            print(">>>> Nota C+")# ele irá imprimir C+ de média.

     elif notas >=80 and notas<=82: # se notas >=80 e <=82
            print(">>>>. Nota B-") # ele irá imprimir B- de bom

     elif notas >=83 and notas<=86: # se notas >=83 e <=86
            print(">>>> Nota B") # ele irá imprimir B de bom

     elif notas >=87 and notas<=89:# se notas >=87 e <=89
            print(">>>> Nota B+") # ele irá imprimir B+ de bom de mais

     elif notas >=90 and notas<=92:# se notas>=90 e <=92
            print(">>>> Nota A-") # ele irá imprimir A- de muito bom

     elif notas >=93 and notas<=96: # se notas>=93 e <=96
            print(">>>> Nota A")  # ele irá imprimir A de excelente   

     elif notas >=97 and notas<=100: # se notas >=97 e <=100
            print(">>>> Nota A+") # ele irá imprimir A+ de superior

     else:
        print("<<<< Nota inválida! Por favor digite uma nota de 0 a 100!>>>>")  #ESTÁ FUNCIONANDO ,Também mudei a ordem de algumas notas e letras no código, da imagem, explicando como são as notas.
        
        print("** Obrigado por ver a sua nota com a gente, volte sempre! **") 
nota()
    


