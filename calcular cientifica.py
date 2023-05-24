#começo calculadora cientifica.


print("<<<<<<<<<<<Bem vindo a calculadora científica>>>>>>>>>>>>")
iniciar=input(" Por favor digite seu nome:\n")

while True:
    print(" Escolha uma opção a seguir")
    comeco=print(" Para as contas básicas:\n'1'\n"
          " para circulos:\n'2'\n"
          " Para equação do segundo grau:\n'3'\n"
         " Para pôtencias e raízes:\n'4'\n"
          "Para conversor de unidade:\n'5'\n"
           "Para geometria:\n'6'\n"
            " Para função:\n'7'\n"
             "Para velocidade média:\n'8\n"
             " Para sair do programa 0")
    opcao=input(" Escolha uma opção: ")
    
    if comeco=='1':
     print(" Bem vindo as contas básicas!")
     print("###### Digite + para soma\n,"
                   " - para subtração,\n"
                    " * para multiplicação,\n "
                    "e / para divisão\n. ##:\n")
    operacao=input(" Digite a operação desejada: \n")
    
    if operacao=="+":
     n1=input(" ###Digite o primeiro número: \n>>>>")
     n2=input("###Digite o segundo número: \n>>>>")
     soma=(n1+n2)
     print(" A soma de ",n1,"+",n2, " é de :",soma)
     print("✦—————♛—————✦")

    elif operacao=="-":
      n1=input(" ###Digite o primeiro número: \n>>>>")
      n2=input("###Digite o segundo número: \n>>>>")
      sub=(n1-n2)
      print(" A subtração de ",n1,"-",n2, " é de :",sub)
      print("✦—————♛—————✦")

    elif operacao=="*":
      n1=input(" ###Digite o primeiro número: \n>>>>")
      n2=input("###Digite o segundo número: \n>>>>")
      mul=(n1*n2)
      print(" A Multiplicação de ",n1,"x",n2, " é de :",mul)
      print("✦—————♛—————✦")  

    elif operacao=="/":
      n1=input(" ###Digite o primeiro número: \n>>>>")
      n2=input("###Digite o segundo número: \n>>>>")
      div=(n1/n2)
      print(" A Divisão de ",n1,"/",n2, " é de :",div)
      print("✦—————♛—————✦")   
              
    else:
      if comeco =="0":
       print(" Obrigada por usar o programa.")
      break