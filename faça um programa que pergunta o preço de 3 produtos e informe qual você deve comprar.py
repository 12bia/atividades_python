
# faça um programa que pergunte o preço de tres produtos e informe qual produto voce deve comprar, sabendo que a decisao e sempre pelo mais barato.

nome=input(" Digite o nome do produto:\n")
pro1=float(input(" Digite o preço do 1 produto:\n"))

nome2=input(" Digite o nome do produto:\n")
pro2=float(input(" Digite o preço do 2 produto:\n"))

nome3=input(" Digite o nome do produto:\n")
pro3=float(input(" Digite o preço do 3 produto:\n"))


if pro1<pro2 and pro1<pro3:
    print(" Compre esse %s pelo Valor %.2f na Americanas"%(nome,pro1))# se digitar menor nesse , ele pega.

elif pro2<pro3 and pro2<pro1:
    print(" Compre esse %s pelo valor %.2f na Magazine Luiza"%(nome2,pro2))# foiii

elif pro3<pro1 and pro3<pro2:
    print(" Compre esse %s pelo valor %.2f na Shopp"%(nome3,pro3))

    # tem que ver se as 2 condições são verdadeiras!, na função...