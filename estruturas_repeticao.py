"""Estruturas de repetição em python"""
import random

lista = ["arroz", "feijão", "cuzcuz", "macarrão"]

for comida in lista:
    print(comida)

for i in range(10):
    print(i)

for i in range(0, 10, 1):
    print(i)

for i in range(1, 10, 2):
    print(i)

print("----------------------------")

contador = 0
while contador < 10:
    print(contador)
    contador += 1

resposta = ""
while resposta != "sim":
    resposta = input("Você está gostando de python?")

print(resposta)

for i in range(1, 10):
    if i == 5:
        continue
    print(i)

for i in range(1, 10):
    if i == 5:
        break
    print(i)

numero_secreto = random.randint(1, 10)
tentativas = 0

while True:
    palpite = int(input("Adivinhe o número entre 1 e 10"))
    tentativas += 1

    if palpite == numero_secreto:
        print(f"Parabens, você acertou o número em {tentativas} tentativas")
        break
    elif palpite < numero_secreto:
        print("Tente um número maior")
    else:
        print("Tente um número menor")
