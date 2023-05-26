#começo calculadora cientifica.


print("<<<<<<<<<<<Bem vindo a calculadora científica>>>>>>>>>>>>")
iniciar=input(" Por favor digite seu nome:\n")

while True:
    print("✦—————♛—————✦✦—————♛—————✦✦—————♛—————✦✦—————♛—————✦✦—————♛—————✦✦—————♛—————✦")
    print(" ▌Escolha uma opção a seguir")
    print(" ▌Para as contas básicas:'1'\n"
          " ▌Para circulos:'2'\n"
          " ▌Para equação do segundo grau:'3'\n"
         " ▌Para pôtencias e raízes:'4'\n"
          " ▌Para conversor de unidade:'5'\n"
           " ▌Para geometria:'6'\n"
            " ▌Para função:'7'\n"
             " ▌Para velocidade média:'8'\n"
             " ▌Para sair do programa :'0'")
    operacao=input(">>>>> Escolha uma opção: ") 
    
    if operacao=='1':
        print(" Bem vindo as contas básicas!")
        print(" ▌Digite + para soma\n"
            " ▌- para subtração\n"
            " ▌* para multiplicação,\n "
            "▌e / para divisão\n")
        op=input(" >>>>>Digite a operação desejada: \n")

        if op=="+":
            n1=int(input(" ###Digite o primeiro número: \n>>>>"))
            n2=int(input("###Digite o segundo número: \n>>>>"))
            soma=(n1+n2)
            print(" A soma de ",n1,"+",n2, " é de :",soma)
            print("✦—————♛—————✦✦—————♛—————✦✦—————♛—————✦✦—————♛—————✦✦—————♛—————✦✦—————♛—————✦")

        elif op=="-":
            n1=int(input(" ###Digite o primeiro número: \n>>>>"))
            n2=int(input("###Digite o segundo número: \n>>>>"))
            sub=(n1-n2)
            print(" A subtração de ",n1,"-",n2, " é de :",sub)
            print("✦—————♛—————✦✦—————♛—————✦✦—————♛—————✦✦—————♛—————✦✦—————♛—————✦✦—————♛—————✦")

        elif op=="*":
            n1=int(input(" ###Digite o primeiro número: \n>>>>"))
            n2=int(input("###Digite o segundo número: \n>>>>"))
            mul=(n1*n2)
            print(" A Multiplicação de ",n1,"x",n2, " é de :",mul)
            print("✦—————♛—————✦✦—————♛—————✦✦—————♛—————✦✦—————♛—————✦✦—————♛—————✦✦—————♛—————✦")  

        elif op=="/":
            n1=int(input(" ###Digite o primeiro número: \n>>>>"))
            n2=int(input("###Digite o segundo número: \n>>>>"))
            div=(n1/n2)
            print(" A Divisão de ",n1,"/",n2, " é de :",div)
            print("✦—————♛—————✦✦—————♛—————✦✦—————♛—————✦✦—————♛—————✦✦—————♛—————✦✦—————♛—————✦")   
     # circunfêrencia do círculo. 
    if operacao=="2":
     print(" ೃ⁀➷Bem vindo ao círculo! ೃ⁀➷")
     raio=float(input(" Digite um valor do raio, para obter a circunferência do círculo:"))
     circunferencia=2*3.14*raio
     print("A circuferência do círculo é de :%.2f "%circunferencia)

     #equação do segundo grau.
    if operacao=="3":
         print(" ೃ⁀➷Bem vindo a Equação do Segundo Grau! ೃ⁀➷")
         def raizes(a, b, c):
            D = (b**2 - 4*a*c)
            x1 = (-b + D**(1/2)) / (2*a)
            x2 = (-b - D**(1/2)) / (2*a)

            print('\nValor de x1: {0}'.format(x1))
            print('Valor de x2: {0}'.format(x2))

    if __name__ == '__main__':
            while True:
                print('Calculando as raízes de uma equação de 2º grau\n')
                a = float(input('Entre com o valor de a: '))
                b = float(input('Entre com o valor de b: '))
                c = float(input('Entre com o valor de c: '))
                raizes(a,b,c)

                continua = input('Deseja sair? Digite q ou Enter para novo cálculo:')
                if (continua == 'q'):
                    break

    if operacao=="4":
        print(" ೃ⁀➷Bem vindo a potência! ೃ⁀➷")




               









    elif operacao=="0":
        print(" Obrigada por usar o programa.")
        break

    #if operacao =="0":