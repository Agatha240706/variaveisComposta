lista1 =[]
mult = 1

while True:
    lista = int(input("Digite 0 para parar, informe o número: "))
    lista1.append(lista)
    if lista == 0:
        lista1.remove(0)
        break

quantidade = len(lista1)
lista1.sort(reverse = True)
print(f'a quantidade é: {quantidade}')
print(f'Ordem decrescente: ',lista1)
if 5 in lista1:
    print("Possui o número 5 no lista")
