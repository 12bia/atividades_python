
# faca um algoritmo que receba 2 notas e calcule a media aritmetica e mostre o resultado(aprovado>=7, recuperação entre 5 e 6,99 e reprovado).

print(" ++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print(">>>>>>>Para ver o seu boletim digite as notas abaixo!<<<<<<<<<<<")
n1=float(input(" Digite a sua nota 1:"))
n2=float(input(" digite a nota 2:"))

media=n1+n2

if media>=7:
    print(" Você foi aprovado!")

elif media==5 and 6.99:
    print(" Você está de recuperação!")

else:
    media<5
    print(" Você está reprovado!")          

print("++++++++++++++++++++++++++++++++++++++++")
