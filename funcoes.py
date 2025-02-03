"""Funções em python"""

def saudacao(nome="Krisofferson"):
    print(f"Olá {nome}, tudo bem?")


def somar(a, b):
    return a + b


def operacoes(a, b):
    soma = a + b
    diferenca = a - b
    return soma, diferenca


x = 3
y = 4

resultado_soma, resultado_diferenca = operacoes(x, y)
print(f"A soma de {x} e {y} é: {resultado_soma}")
print(f"A diferença entre {x} e {y} é: {resultado_diferenca}")


def calcular_media(nota_a, nota_b, nota_c):
    media = (nota_a + nota_b + nota_c) / 3
    return media


media_aluno = calcular_media(8, 9, 7)
print(f"A média do aluno é: {media_aluno}")

saudacao("Marini")
saudacao()

somar(4, 3)
