import pickle

def extrair_dados(lista_enderecos):
    
    if not isinstance(lista_enderecos, list):
        raise TypeError
    
    resultado = []
    for endereco in lista_enderecos:
        if 'cep' not in endereco or 'localidade' not in endereco or 'estado' not in endereco:
            raise KeyError
        
        tupla_endereco = (endereco['cep'], endereco['localidade'], endereco['estado'])
        resultado.append(tupla_endereco)
    
    return resultado

with open("exercicio02.bin", "rb") as arquivo:
    dados_cep = pickle.load(arquivo)

print(extrair_dados(dados_cep))
