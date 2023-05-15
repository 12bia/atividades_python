# fazer um algoritimo que ao receber o salario atual de um funcionario, calcule o valor do novo salario reajustado de acordo com a tebela abaixo:
# mostre o salario atual e o anterior, bem como a taxa de areajuste.
# tabela.
# salario atual. abaixo de 500,00 reais- reajuste de 15%
# de 500 ate 1.00000- 10%
# acima de 100000- 5%

sala_atual=float(input(" digite seu salário:"))

if sala_atual<500:
    n1=sala_atual*15/100+sala_atual
    print("Parabéns seu salário teve um aumento de 15 %% e deixou de ser de %.2f para : %.2f"%(sala_atual,n1))

elif sala_atual==500 and 10000:
    n2=sala_atual*10
    print("Parabéns seu salário teve um aumento de 10 %% e deixou de ser de %.2f para: %.2f"%(sala_atual,n2))

elif sala_atual>10000:
    n3=sala_atual*5
    print ("Parabéns seu salário teve um aumento de 5 %% e deixou de ser de %.2f para: %.2f"%(sala_atual,n3))
