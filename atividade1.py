atend = 0
atendmax = 0
atendmin = 0
cont = 0
contot = 0
contb = 0
contr = 0
contp = 0
idade = 0
idademin = 200
idademax = 0

while (True):
    atend = input("O que achou do atendimento?: (otimo, bom, regular, pessimo)")
    idade = int(input("Qual a sua idade?"))
    if atend == "otimo":
        contot += 1
    if atend == "bom":
        contb += 1
    if atend == "regular":
        contr += 1
    if atend == "pessimo":
        contp += 1
    if idade > idademax:
        idademax = idade
        if idademax:
            atendmax = atend
    if idade < idademin:
        idademin = idade
        if idademin:
            atendmin = atend
    cont += 1
    if (input("continuar? (s,n)")) != "s":
        break
print("Quantidade de pessoas que responderam:", cont)
print("Quantidade de pessoas que reponderam otimo:", contot)
print("Quantidade de pessoas que reponderam bom:", contb)
print("Quantidade de pessoas que reponderam regular:", contr)
print("Quantidade de pessoas que reponderam pessimo:", contp)
print("A pessoa mais velha que respondeu tem:", idademax, "anos .E sua resposta foi:",atendmax)
print("A pessoa mais velha que respondeu tem:", idademin, "anos .E sua resposta foi:",atendmin)