num = []
while True:
    escolha = int(input("Adicione um número: "))
    for i in num:
        if escolha in num:
            num.remove(i)
    num.append(escolha)
    sair = str(input("Quer sair?"))
    if sair == "s":
        break
num.sort()
print(num)
