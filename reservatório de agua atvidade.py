# erxercicio de arrumar o programa da caixa de agua.

print("-- Reservartório de Água --")

altura=float(input(" Digite a altura (cm):"))
largura=float(input(" Digite a largura (cm): "))
comprimento=float(input(" Digite o comprimento (cm): "))
c_diario =float(input("Digite o valor do consumo médio diário(litros/dia)= "))

cap_total=((altura*largura*comprimento/1000)); '''o resultado seria em cm3 por isso, dividimos por mil para passar de cm3 para litros'''
auto_reser=cap_total/c_diario

print("Capacidade do Reservatório= %.2f"%cap_total, "litros ")
print("Autonomia do reservatório= ",auto_reser," dias") ;'''Agora, vamos classificar o consumo'''

if(auto_reser<2):
 print("Consumo Elevado")
elif(auto_reser>=2 and auto_reser<=7):
     print("Consumo Moderado")
else:
    print("\n Consumo Baixo")