map = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' '],
]

line_treasure = 0
column_treasure = 1

def showmap():
    for line in map:
        print('|'.join(line))
        print('-' * 5)

tentativas = 5

print("Caca ao Tesouro Espacial")
print("Encontre o 💎 escondido no tabuleiro 3x3.")
print("Use numeros de 0 a 2 para linha e coluna.")
print("Exemplo: linha 1, coluna 2")

for i in range(tentativas):
    print(f"\nTentativa {i+1} de {tentativas}")

    line = int(input("Digite a linha (0 a 2): "))
    column = int(input("Digite a coluna de (0 a 2)"))


    if line < 0 or line > 2 or column < 0 or column > 2:
       print("Jogada Invalida! Tente valores entre 0 e 2")
       continue

    if line == line_treasure and column == column_treasure:
        map[line][column] = '💎' 
        print("\n Parabens!! Voce encontrou o tesouro!!")
        showmap()
        break
    else:
        if map[line][column] != ' ':
            print("Voce ja tentou aqui!")
        else:
            map[line][column] = 'X'
            print("Continue tentando rs")
        showmap()

else:
    print("\n Tentativas terminaram")
    map[line_treasure][column_treasure] = '💎'
    print("Tesouso aqui rs")
    showmap()