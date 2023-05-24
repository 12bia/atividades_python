
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
op="-1"


while True:
    print("『♡』•『♡』•『♡』•『♡』")
    print("☀ Selecione a opção!☀")
    op = input("Digite 1 para cadastro, \n 2- para consulta, \n 3- para excluir a matrícula,\n ou 0 para sair:")
    if op == "0":
        break
    elif op=="1":
     print("『♡』•『♡』•『♡』•『♡』")
     print(" Bem vindo ao Cadastro")

     nome=input(" Digite seu nome:""\n ˚₊· ͟͟͞͞➳❥ ")
     listanome.append(nome)
            
     sobre=input(" Digite seu sobrenome:""\n ˚₊· ͟͟͞͞➳❥ ")
     listasobre.append(sobre)

        
     endere=input(" Rua:""\n ˚₊· ͟͟͞͞➳❥ ")
     listaendere.append(endere)


     endereco=float(input(" Número:""\n ˚₊· ͟͟͞͞➳❥ "))
     listaendereco.append(endereco)
            
     bai=input(" Digite seu bairro:""\n ˚₊· ͟͟͞͞➳❥ ")
     listabai.append(bai)

        
     cida=input(" Cidade:""\n ˚₊· ͟͟͞͞➳❥ ")
     listacida.append(cida)


     esta=input(" Estado:""\n ˚₊· ͟͟͞͞➳❥ ")
     listaesta.append(esta)

     pais=input(" País:""\n ˚₊· ͟͟͞͞➳❥ ")
     listapais.append(pais)

     fone=float(input(" Digite seu telefone:""\n ˚₊· ͟͟͞͞➳❥ "))
     listafone.append(fone)

     cpf=input(" Digite seu cpf:""\n ˚₊· ͟͟͞͞➳❥ ")
     listacpf.append(cpf)

     peso=float(input(" Digite seu peso:""\n ˚₊· ͟͟͞͞➳❥ "))
     listapeso.append(peso)

     altura=float(input(" Digite sua altura:""\n ˚₊· ͟͟͞͞➳❥ "))
     listaaltura.append(altura)

     idade=int(input(" Digite sua idade:""\n ˚₊· ͟͟͞͞➳❥ "))
     listaidade.append(idade)

     cartao=float(input(" Digite o número do cartão:""\n ˚₊· ͟͟͞͞➳❥ "))
     listacartao.append(cartao)


     email=str(input(" Digite seu E-mail: ""\n ˚₊· ͟͟͞͞➳❥ "))
     listaemail.append(email)

     cep=float(input(" Digite seu CEP:""\n ˚₊· ͟͟͞͞➳❥ "))
     listacep.append(cep)

     print("『♡』•『♡』•『♡』•『♡』")
     print(" Bem vindo ao sistema de notas!")
     n1=float(input(" Digite a nota 1:""\n ˚₊· ͟͟͞͞➳❥ "))
     listan1.append(n1)

     n2=float(input(" Digite a nota 2:""\n ˚₊· ͟͟͞͞➳❥ "))
     listan2.append(n2)

     n3=float(input(" Digite a nota 3:""\n ˚₊· ͟͟͞͞➳❥ "))
     listan3.append(n3)

     n4=float(input(" Digite a nota 4:""\n ˚₊· ͟͟͞͞➳❥ "))
     listan4.append(n4)

     media=(n1+n2+n3+n4)/4
     listamedia.append(media)

     print("『♡』•『♡』•『♡』•『♡』")
     serie=input(" Digite sua série:""\n ˚₊· ͟͟͞͞➳❥ ")
     listaserie.append(serie)

     classe=input(" Digite sua classe:""\n ˚₊· ͟͟͞͞➳❥ ")
     listaclasse.append(classe)

     sexo=input(" Digite seu sexo:""\n ˚₊· ͟͟͞͞➳❥ ")
     listasexo.append(sexo)

     cor=input(" Digite sua cor:""\n ˚₊· ͟͟͞͞➳❥ ")
     listacor.append(cor)

     cont=cont+1    
     listamatricula.append(cont)

     print("▌ Nome:" ,listanome)
     print("▌ Sobrenome: ",listasobre)
     print("▌ Rua:",listaendere)
     print("▌ Número:",listaendereco)
     print("▌ Bairro:",listabai)
     print("▌ Cidade:",listacida)
     print("▌ Estado:",listaesta)
     print("▌ País :",listapais)
     print("▌ Telefone:",listafone)
     print("▌ Cpf:",listacpf)
     print("▌ Peso:",listapeso)
     print("▌ Altura:",listaaltura)
     print("▌ Idade:",listaidade)
     print("▌ Cartão de crédito:",listacartao)
     print("▌ Email:",listaemail)
     print("▌ CEP:",listacep)
     print("▌ Nota 1:",listan1)
     print("▌ Nota 2:",listan2)
     print("▌ Nota 3:",listan3)
     print("▌ Nota 4:",listan4)
     print("▌ Sua média é de:",listamedia)
     print("▌ Série:",listaserie)
     print("▌ Classe:",listaclasse)
     print("▌ Sexo:",listasexo)
     print("▌ Cor :",listacor)
     print("▌ Matrícula:",listamatricula)

    elif op=="2":
      print("☆★☆★→ Bem vindo a matrícula! ←☆★☆★")
      busca=int(input(" Digite sua matrícula: ""\n"))
      print("▌ Nome:" ,listanome[busca-1])
      print("▌ Sobrenome: ",listasobre[busca-1])
      print("▌ Rua:",listaendere[busca-1])
      print("▌ Número:",listaendereco[busca-1])
      print("▌ Bairro:",listabai[busca-1])
      print("▌ Cidade:",listacida[busca-1])
      print("▌ Estado:",listaesta[busca-1])
      print("▌ País :",listapais[busca-1])
      print("▌ Telefone:",listafone[busca-1])
      print("▌ Cpf:",listacpf[busca-1])
      print("▌ Peso:",listapeso[busca-1])
      print("▌ Altura:",listaaltura[busca-1])
      print("▌ Idade:",listaidade[busca-1])
      print("▌ Cartão de crédito:",listacartao[busca-1])
      print("▌ Email:",listaemail[busca-1])
      print("▌ CEP:",listacep[busca-1])
      print("▌ Nota 1:",listan1[busca-1])
      print("▌ Nota 2:",listan2[busca-1])
      print("▌ Nota 3:",listan3[busca-1])
      print("▌ Nota 4:",listan4[busca-1])
      print("▌ Sua média é de:",listamedia[busca-1])
      print("▌ Série:",listaserie[busca-1])
      print("▌ Classe:",listaclasse[busca-1])
      print("▌ Sexo:",listasexo[busca-1])
      print("▌ Cor :",listacor[busca-1])
      print("▌" " sua matrícula é :",listamatricula[busca-1])  

    if op=="3":
       delete=int(input(" Digite a matrícula a ser excluída:"))
       del(listamatricula[delete-1], listanome[delete-1],listasobre[delete-1],listaendere[delete-1],listaendereco[delete-1],listabai[delete-1],listacida[delete-1],listaesta[delete-1],listapais[delete-1],listafone[delete-1],listacpf[delete-1],listapeso[delete-1],listaaltura[delete-1],listaidade[delete-1],listacartao[delete-1],listaemail[delete-1],listacep[delete-1],listan1[delete-1],listan2[delete-1],listan3[delete-1],listan4[delete-1],listamedia[delete-1],listaserie[delete-1],listaclasse[delete-1],listasexo[delete-1],listacor[delete-1])
       print(" A matrícula ",delete," foi excluída.")

'''listamatricula= ["0","1","2","3","4","5","6","7","8","9","10","11"]
print(listamatricula[1:3])
print(listamatricula[:4])
print(listamatricula[3:])
print(listamatricula[:])
print(listamatricula[0:6])'''


