# faça um programa para a leitura de duas notas parciais de um aluno. o programa deve calcular a media alcançada por aluno e apresentar: a mensagem " Aprovado", se a media alcançada for maior ou igual a sete.
# a mensagem " Reprovado" , se a media for menor do que sete.
# a mensagem " Distinção", se a media for igual a 10


n1=float(input(" Digite a nota 1:"))
n2=float(input(" Digite a nota 2:"))

media=(n1+n2)/2

if media>=7:
    print(" Aprovado")

elif media<=7:
    print(" reprovado")   

if media==10:
    print(" distinção") 

   

