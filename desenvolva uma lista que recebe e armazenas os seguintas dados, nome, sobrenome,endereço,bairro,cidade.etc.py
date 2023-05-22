
# Desenvolva um algoritmo que receba e armazene em uma lista,  posterirormente imprima os seguintes dados:
# nome,sobrenome,endereço(rua,n), bairro,cidade,,estado,pais,telefone,cpf,peso,altura,idade,numero de cartas, email,cep,nota1,nota2,nota3,nota4,media,serie,classe,sexo,cor,matricula automática.
# a matrícula automática é pra fazer automática.
lista=[]
listanome=[]
listasobre=[]
listaendere=[]
listaendereco=[]
listabai=[]
listacida=[]
listaesta=[]
listapais=[]
listafone=[]
listacpf=[]
listapeso=[]
listaaltura=[]
listaidade=[]
listacartao=[]
listaemail=[]
listacep=[]
listan1=[]
listan2=[]
listan3=[]
listan4=[]
listamedia=[]
listaserie=[]
listaclasse=[]
listasexo=[]
listacor=[]
listamatricula=[]
cont=0


while True:
    op = input("Digite 1 para cadastro ou 0 para sair:")
    if op == "0":
        break
    elif op=="1":
        print(" Bem vindo ao Anonimous, por favor preencha o cadastro abaixo para sabermos tudo da sua vida!")

        nome=input(" Digite seu nome:""\n")
        listanome.append(nome)
        
        sobre=input(" Digite seu sobrenome:""\n")
        listasobre.append(sobre)

    
        endere=input(" Rua:")
        listaendere.append(endere)


        endereco=float(input(" Número;"))
        listaendereco.append(endereco)
        
        
        
    
        bai=input(" Digite seu bairro:")
        listabai.append(bai)

    
        cida=input(" Cidade:")
        listacida.append(cida)


        esta=input(" Estado:")
        listaesta.append(esta)

        pais=input(" País:")
        listapais.append(pais)

        fone=float(input(" Digite seu telefone:"))
        listafone.append(fone)

        cpf=input(" Digite seu cpf:")
        listacpf.append(cpf)

        peso=float(input(" Digite seu peso:"))
        listapeso.append(peso)

        altura=float(input(" Digite sua altura:"))
        listaaltura.append(altura)

        idade=int(input(" Digite seu idade:"))
        listaidade.append(idade)

        cartao=float(input(" Digite o número do cartão:"))
        listacartao.append(cartao)


        email=str(input(" Digite seu E-mail: "))
        listaemail.append(email)

        cep=float(input(" Digite seu CEP:"))
        listacep.append(cep)

        print(" Bem vindo ao sistema de notas!")
        n1=float(input(" Digite a nota 1:"))
        listan1.append(n1)

        n2=float(input(" Digite a nota 2:"))
        listan2.append(n2)

        n3=float(input(" Digite a nota 3:"))
        listan3.append(n3)

        n4=float(input(" Digite a nota 4:"))
        listan4.append(n4)

        media=(n1+n2+n3+n4)/4
        listamedia.append(media)

        serie=input(" Digite sua série:")
        listaserie.append(serie)

        classe=input(" Digite sua classe:")
        listaclasse.append(classe)

        sexo=input(" Digite seu sexo:")
        listasexo.append(sexo)

        cor=input(" Digite sua cor:")
        listacor.append(cor)

        cont=cont+1    
        listamatricula.append(cont)

        print(" Nome:" ,listanome)
        print(" Sobrenome: ",listasobre)
        print(" Rua:",listaendere)
        print(" Número:",listaendereco)
        print(" Bairro:",listabai)
        print(" Cidade:",listacida)
        print(" Estado:",listaesta)
        print(" País :",listapais)
        print(" Telefone:",listafone)
        print(" Cpf:",listacpf)
        print(" Peso:",listapeso)
        print(" Altura:",listaaltura)
        print(" Idade:",listaidade)
        print(" Cartão de crédito:",listacartao)
        print(" Email:",listaemail)
        print(" CEP:",listacep)
        print(" Nota 1:",listan1)
        print(" Nota 2:",listan2)
        print(" Nota 3:",listan3)
        print(" Nota 4:",listan4)
        print(" Sua média é de:",listamedia)
        print(" Série:",listaserie)
        print(" Classe:",listaclasse)
        print(" Sexo:",listasexo)
        print(" Cor :",listacor)
        print(" Matrícula:",listamatricula)


        
'''listamatricula= ["0","1","2","3","4","5","6","7","8","9","10","11"]
print(listamatricula[1:3])
print(listamatricula[:4])
print(listamatricula[3:])
print(listamatricula[:])
print(listamatricula[0:6])'''