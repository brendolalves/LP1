import pickle

def listar_nomes_personagens(dados):
    
    resultado = []
    for personagem in dados:
        nome = personagem.get('name')
        resultado.append(nome)
    return resultado


with open("exercicio04.bin", "rb") as arquivo:
    dados = pickle.load(arquivo)

