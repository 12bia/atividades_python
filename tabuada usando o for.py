# desenvolva uma calculadora de multiplicação com o for aninhado, não esqueça de seguir o padrão de impressão.

for i in range(1,11):
    print("="*12)
    for j in range(1,11):
        resul=(i*j)
        print(i,"x",j,"=",resul)

 # utilizando o para (for) efetue uma contagem de o até 100, porem somente com numeros pares.

for i in range(1,100,2):
    print("="*12)
    print(i)      
##################################################
# faça um programa que receba dois numeros inteiros e gere os numeros inteiros que estão no intervalo compreendido por eles.

ini=int(input(" Digite um número inicial:"))
fi=int(input(" Digite o número final:"))

for i in range(ini,fi):
    print(i)

# ele vai imprimir assim: se a pessoa digitar inicial 2, e final 5
'''2
3
4
5'''