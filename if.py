#funcões  do if, como usar o if


idade=18
if idade<20:
    print(" Você é jovem!\n")
    ###############################################3333

    idade=int(input(" Digite sua idade:"))
    if (idade<=19):
        print(" Você é de menor!")
    else:
        print(" Você é de maior!")    
#########################################################33
age=18
if(age>17):
    print(" Você é de maior, já pode dirigir")
    print(" Fim.fora do if")
######################################

idade=int(input(" Digite sua idade:"))
if idade==16:
    print(" Pode votar!")
else:
    if idade>=16:
        print(" Pode dirigir!")
    else:
        if idade<16:
            print(" Só estuda meu filho!")

####################################

idade=int(input(" Digite sua idade:"))
if idade>=16 and idade<18:
    print(" Pode votar!")
elif idade<16:
    print(" apenas estude!")
else:
    print(" Pode dirigir.")

    #########################################
 # ==, igual a 

    #(and) e
    #(our)ou

    
