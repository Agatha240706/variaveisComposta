num1 =[]
mult = 1
while True:
    num = int(input("Digite os números(Digite 0 se deseja parar):"))
    num1.append(num)
    if num == 0:
        num1.remove(0)
        break

soma = sum(num1)
maior = max(num1)
menor = min(num1)

for c in num1:
    mult *= c

print("soma dos números é:",soma)
print("multiplicação: ",mult)
print("maior número é:",maior)
print("menor número é: ",menor)