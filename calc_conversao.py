# calc_conversao.py

#Módulo E - Conversão

#Autor: João Eliézer

#Branch: feature/operacoes_conversao

def celsius_para_fahrenheit(celsius):
    try:
        return (celsius * 9/5) + 32
    except TypeError:
        raise ValueError("O valor deve ser um número.")
    except Exception as e:
        raise RuntimeError(f"Ocorreu um erro inesperado: {e}")

def km_para_milhas(km):
    try:
        return km * 0.621371
    except TypeError:
        raise ValueError("O valor deve ser um número.")
    except Exception as e:
        raise RuntimeError(f"Ocorreu um erro inesperado: {e}")

def kg_para_libras(kg):
    try:
        return kg * 2.20462
    except TypeError:
        raise ValueError("O valor deve ser um número.")
    except Exception as e:
        raise RuntimeError(f"Ocorreu um erro inesperado: {e}")

