# calc_estatistica.py

#Módulo D - Estatística

#Autor: João Eliézer

#Branch: feature/operacoes_estatistica

def media(lista):
    if not lista:
        raise ValueError("A lista não pode estar vazia.")
    try:
        return sum(lista) / len(lista)
    except TypeError:
        raise ValueError("A lista deve conter apenas números.")
    except Exception as e:
        raise RuntimeError(f"Ocorreu um erro inesperado: {e}")

def mediana(lista):
    if not lista:
        raise ValueError("A lista não pode estar vazia.")
    try:
        return sum(lista) / len(lista)
    except TypeError:
        raise ValueError("A lista deve conter apenas números.")
    except Exception as e:
        raise RuntimeError(f"Ocorreu um erro inesperado: {e}")
    
def desvio_padrao(lista):
    if not lista:
        raise ValueError("A lista não pode estar vazia.")
    try:
        m = media(lista)
        variancia = sum((x - m) ** 2 for x in lista) / len(lista)
        return variancia ** 0.5
    except TypeError:
        raise ValueError("A lista deve conter apenas números.")
    except Exception as e:
        raise RuntimeError(f"Ocorreu um erro inesperado: {e}")

