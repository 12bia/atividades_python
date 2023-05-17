# faça um programa que pergunte o preço de tres produtos e informe qual produto voce deve comprar, sabendo que a decisao e sempre pelo mais barato.

nome=input(" Digite o nome do produto:\n")

pro1=float(input(" Digite o preço do 1 produto:\n"))
pro2=float(input(" Digite o preço do 2 produto:\n"))
pro3=float(input(" Digite o preço do 3 produto:\n"))


if pro1>pro2:
    print(" Compre esse na Americanas",pro1)# se digitar menor nesse , ele pega.

elif pro2<pro3:
    print(" Compre esse na Magazine Luiza",pro2)# foiii

elif pro3>pro1:
    print(" Compre esse  na Shopp",pro3) 


    #elif  pro3<pro1: