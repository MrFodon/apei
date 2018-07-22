print("Escolha uma operação matemática")
print("Soma - digite 0")
print("Subtração - digite 1")
print("Divisão - digite 2")
print("Multiplicação - digite 3")
print("Potenciação - digite 4")

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite outro número: "))

escolha = int(input("Digite uma opção: "))

if escolha == 0:
    soma = num1 + num2
    print("Resultado %i" %soma)
if escolha == 1:
    subtração = num1 - num2
    print("Resultado %i" %subtração)
if escolha == 2:
    divisão = num1 / num2
    print("Resultado %f" %divisão)
if escolha == 3:
    multiplicação = num1 * num2
    print("Resultado %i" %multiplicação)
if escolha == 4:
    potência = num1 ** num2
    print("Resultado %i" %potência)

    
