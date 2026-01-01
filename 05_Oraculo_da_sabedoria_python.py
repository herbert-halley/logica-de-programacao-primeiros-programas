print("Bom dia como posso ajudar voce hoje? Aqui quem fala eh o assistente do ChatGpt 1.0")

comando = input("Digite o comando: ")

match comando:
    case "palmeiras tem mundial?" | "Palmeiras tem mundial?" | "O Palmeiras tem mundial" :
        print ("A Fifa Nao reconhece que o Palmeiras tem mundial.")
    case "Quantas Libertadores o Sao Paulo Tem?" | "Quantos mundiais o Sao Paulo tem?" :
        print (3)
    case _:
        print("Nao tenho essa resposta na minha base de dados")