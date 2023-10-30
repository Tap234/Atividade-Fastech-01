elevador = 0
elea = 0
eleb = 0
elec = 0
periodo = 0
perma = 0
perva = 0
perna = 0
permb = 0
pervb = 0
pernb = 0
permc = 0
pervc = 0
pernc = 0
permt = 0
pervt = 0
pernt = 0
while (True):
    elevador = input("Qual elevador você utiliza com maior frequencia?(a, b, c)")
    periodo = input("Em qual periodo do dia você mais utiliza o elevador?(matutino, vespertino, noturno)")
    if elevador == "a":
        elea += 1
        if periodo == "matutino":
            perma += 1
        if periodo == "vespertino":
            perva += 1
        if periodo == "noturno":
            perna += 1
    if elevador == "b":
        eleb += 1
        if periodo == "matutino":
            permb += 1
        if periodo == "vespertino":
            pervb += 1
        if periodo == "noturno":
            pernb += 1
    if elevador == "c":
        elec += 1
        if periodo == "matutino":
            permc += 1
        if periodo == "vespertino":
            pervc += 1
        if periodo == "noturno":
            pernc += 1
    if periodo == "matutino":
        permt += 1
    if periodo == "vespertino":
        pervt += 1
    if periodo == "noturno":
        pernt += 1
    if input("deseja continuar?(s,n)") != "s":
        break
# A
if elea > eleb:
    if elea > elec:
        if perma > perva:
            if perma > perna:
                print("O elevador mais utilizado é o A. E o periodo é o matutino")
        if perva > perma:
            if perva > perna:
                print("O elevador mais utilizado é o A. E o periodo é o vespertino")
        if perna > perva:
            if perna > perma:
                print("O elevador mais utilizado é o A. E o periodo é o noturno")
        if perma == perva > perna:
            print("O elevador mais utilizado é o A. E o periodo é o matutino e o vespertino silmutaneamente")
        if perma == perna > perva:
            print("O elevador mais utilizado é o A. E o periodo é o matutino e o noturno silmutaneamente")
        if perva == perna > perma:
            print("O elevador mais utilizado é o A. E o periodo é o noturno e o vespertino silmutaneamente")
        if perma == perva == perna:
            print("O elevador mais utilizado é o A. E o periodo é o matutino, vespertino e o noturno silmutaneamente")
# B
if eleb > elea:
    if eleb > elec:
        if permb > pervb:
            if permb > pernb:
                print("O elevador mais utilizado é o B. E o periodo é o matutino")
        if pervb > permb:
            if pervb > pernb:
                print("O elevador mais utilizado é o B. E o periodo é o vespertino")
        if pernb > permb:
            if pernb > pervb:
                print("O elevador mais utilizado é o B. E o periodo é o noturno")
        if permb == pervb > pernb:
            print("O elevador mais utilizado é o B. E o periodo é o matutino e o vespertino silmutaneamente")
        if permb == pernb > pervb:
            print("O elevador mais utilizado é o B. E o periodo é o matutino e o noturno silmutaneamente")
        if pervb == pernb > permb:
            print("O elevador mais utilizado é o B. E o periodo é o noturno e o vespertino silmutaneamente")
        if permb == pervb == pernb:
            print("O elevador mais utilizado é o B. E o periodo é o matutino, vespertino e o noturno silmutaneamente")
# C
if elec > elea:
    if elec > eleb:
        if permc > pervc:
            if permc > pernc:
                print("O elevador mais utilizado é o C. E o periodo é o matutino")
        if pervc > permc:
            if pervc > pernc:
                print("O elevador mais utilizado é o C. E o periodo é o vespertino")
        if pernc > permc:
            if pernc > pervc:
                print("O elevador mais utilizado é o C. E o periodo é o noturno")
        if permc == pervc > pernc:
            print("O elevador mais utilizado é o C. E o periodo é o matutino e o vespertino silmutaneamente")
        if permc == pernc > pervc:
            print("O elevador mais utilizado é o C. E o periodo é o matutino e o noturno silmutaneamente")
        if pervc == pernc > permc:
            print("O elevador mais utilizado é o C. E o periodo é o noturno e o vespertino silmutaneamente")
        if permc == pervc == pernc:
            print("O elevador mais utilizado é o C. E o periodo é o matutino, vespertino e o noturno silmutaneamente")
if elea == eleb > elec:
    print("O elevador mais utilizado é o A e B")
if eleb == elec > elea:
    print("O elevador mais utilizado é o B e C")
if elea == elec > eleb:
    print("O elevador mais utilizado é o A e C")
if elea == eleb == elec:
    print("O elevador mais utilizado é o A , B e C")
if permt > pervt:
    if permt > pernt:
        print("O perído em que o elevador mais foi usado é: Matutino")
if pervt > permt:
    if pervt > pernt:
        print("O perído em que o elevador mais foi usado é: Vespertino")
if pernt > permt:
    if pernt > pervt:
        print("O perído em que o elevador mais foi usado é: Noturno")
if permt == pervt > pernt:
    print("O perído em que o elevador mais foi usado é: Matutino e Vespertino")
if permt == pernt > pervt:
    print("O perído em que o elevador mais foi usado é: Matutino e Noturno")
if pernt == pervt > permt:
    print("O perído em que o elevador mais foi usado é: Vespertino e Noturno")
if permt < pervt:
    if permt < pernt:
        print("O perído em que o elevador menos foi usado é: Matutino")
if pervt < permt:
    if pervt < pernt:
        print("O perído em que o elevador menos foi usado é: Vespertino")
if pernt < permt:
    if pernt < pervt:
        print("O perído em que o elevador menos foi usado é: Noturno")
if permt == pervt < pernt:
    print("O perído em que o elevador menos foi usado é: Matutino e Vespertino")
if permt == pernt < pervt:
    print("O perído em que o elevador menos foi usado é: Matutino e Noturno")
if pernt == pervt < permt:
    print("O perído em que o elevador menos foi usado é: Vespertino e Noturno")
