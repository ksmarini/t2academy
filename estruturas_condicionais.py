nome = "Marini" # str
idade = 44 # int
altura = 1.75 # float
eh_estudante = True # bool

if idade < 16:
    print("Não pode votar")
elif idade < 18 or idade >= 65:
    print("Voto facultativo")
else:
    print("Voto obrigatório")

if idade == altura:
    print("idade igual altura")

if idade != altura:
    print("idade diferente altura")

if not idade < 18:
    print('Tá velho')
