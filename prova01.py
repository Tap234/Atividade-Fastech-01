cor = 0
idade = 0
idademaxa = 0
idademina = 200
idademaxv = 0
idademinv = 200
idademaxr = 0
idademinr = 200
sexo = 0
sexoma = 0
sexofa = 0
sexomv = 0
sexofv = 0
sexomr = 0
sexofr = 0
cont = 0
conta = 0
contv = 0
contr = 0

while (True):
    cor = input("Qual a sua cor preferida? a=Azul, v=Verde ou r=Rosa ")
    idade = int(input("Qual a sua idade? "))
    sexo = input("Qual o seu sexo? m=masculino ou f=feminino ")
    cont += 1
    if cor == "a":
        conta += 1
        if idademaxa < idade:
            idademaxa = idade
        if idademina > idade:
            idademina = idade
        if sexo == "m":
            sexoma += 1
        if sexo == "f":
            sexofa += 1
    if cor == "v":
        contv += 1
        if idademaxv < idade:
            idademaxv = idade
        if idademinv > idade:
            idademinv = idade
        if sexo == "m":
            sexomv += 1
        if sexo == "f":
            sexofv += 1
    if cor == "r":
        contr += 1
        if idademaxr < idade:
            idademaxr = idade
        if idademinr > idade:
            idademinr = idade
        if sexo == "m":
            sexomr += 1
        if sexo == "f":
            sexofr += 1
    if input("Continuar? s ou n ") != "s":
        break
print(cont, "Pessoas responderam")
print(conta/cont*100, "% Preferem a cor Azul")
print(contv/cont*100, "% Preferem a cor Verde")
print(contr/cont*100, "% Preferem a cor Rosa")
if idademaxa != 0:
    print("A pessoa mais velha que prefere o azul tem", idademaxa, "Anos")
if idademina != 200:
    print("A pessoa mais nova que prefere o azul tem", idademina, "Anos")
if idademaxv != 0:
    print("A pessoa mais velha que prefere o verde tem", idademaxv, "Anos")
if idademinv != 200:
    print("A pessoa mais nova que prefere o verde tem", idademinv, "Anos")
if idademaxr != 0:
    print("A pessoa mais velha que prefere o rosa tem", idademaxr, "Anos")
if idademinr != 200:
    print("A pessoa mais nova que prefere o rosa tem", idademinr, "Anos")
if sexoma != 0:
    print(sexoma, "Pessoa(s) do sexo masculino prefere(m) azul")
if sexofa != 0:
    print(sexofa, "Pessoa(s) do sexo feminino prefere(m) azul")
if sexomv != 0:
    print(sexomv, "Pessoa(s) do sexo masculino prefere(m) verde")
if sexofv != 0:
    print(sexofv, "Pessoa(s) do sexo feminino prefere(m) verde")
if sexomr != 0:
    print(sexomr, "Pessoa(s) do sexo masculino prefere(m) rosa")
if sexofr != 0:
    print(sexofr, "Pessoa(s) do sexo feminino prefere(m) rosa")
