
# faça um programa que verifique se uma letra digitada é f , m ou o. conforme a letra escrever : f- femininio, m - masculino, o- outros ou sexo invalido.

print("=======================================================")
letra=input(" Digite 'F' para Feminino, 'M' para Masculino e 'O' para Outros.")

if letra =="f" and "F":
    print(" >>>>>>>>>>>FEMININO!<<<<<<<<<<<")

    print("=======================================================")
elif letra =="m" and " M":
    print(" >>>>>>>>>MASCULINO<<<<<<<<")

    print("=======================================================")
elif letra =="o" and " O":
    print(" >>>>>>>>OUTROS<<<<<<")
    print("=======================================================")
    
else:
    print(" >>>>>>>>>>>SEXO INVÁLIDO!<<<<<<<")