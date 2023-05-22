#calculadora cheia de função e problemas.py

#ATIVIDADES PYTHON CALCULADORA 2.0


while in!=0

n1 = float(input("Primeiro número:"))
n2 = float(input("Segundo número:"))
operacao = input(" Escolha uma operação: digite + para soma,"
                 " - para subtração, * para multiplicação, / para divisão")
                   

def calculadora(n1,n2,operacao):
  if operacao == "+":
    resultado = n1 + n2
  elif operacao == "-":
    resultado = n1 - n2
  elif operacao == "*":
    resultado = n1 * n2
  elif operacao == "/":
    resultado = n1 / n2
  elif operacao=="V"and "v":
    resultado= n1
  else:
    print("Operação inválida!")
resultado = 0
print("Resultado: ", resultado)

" V para volume de um cubo, E para exponenciação,"
                   " R para  raiz quadrada, A para área do quadrado,"
                   " e F para fatoração.")