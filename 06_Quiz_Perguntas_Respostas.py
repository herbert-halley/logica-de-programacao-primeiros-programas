perguntas = [
    ["Palmeiras tem mundial?", "Nao"],
    ["Quanto eh 2 + 2 / 2 ?", "3"],
    ["Qual eh o nome do maior planeta do nosso sistema solar?", "jupiter"],
    ["Qual eh o nome do menor planeta do  nosso sistema solar?", "plutao"],
    ["Qual fruta remete ao macaco?", "banana"],
    ["Qual a cor eh formada com a juncao da cor amarela + cor vermelha?", "laranja"]
]

acertos = 0

for pergunta in perguntas:
    resposta = input(pergunta[0] + " ")
    if resposta.lower() == pergunta[1]:
        acertos += 1

print(f"Voce acertou {acertos} de {len(perguntas)} perguntas!")