#faça um programa que digite uma letra e veja se é vogal ou consoante.py

print(" Bem vindoo!")
letra=input(" Por favor digite uma letra:")
letra = letra.lower()
if letra=="a" or letra=="e" or letra=="i" or letra=="o"  or letra=="u":
    print("A letra que você digitou ",letra," é vogal!")

else:
    print(" A letra que você digitou ",letra, " é consoante!")   

