# calc_percentual.py

#Módulo C - Percentual

#Autor: João Eliézer

#Branch: feature/operacoes_percentual

def percentual(percentual, valor):
    try:
        return (percentual / 100) * valor
    except TypeError:
        raise ValueError("Os operandos devem ser números.")

def acrescimo(percentual, valor):
    try:
        return valor + percentual(percentual, valor)
    except TypeError:
        raise ValueError("Os operandos devem ser números.")

def desconto(percentual, valor):
    try:
        return valor - percentual(percentual, valor)
    except TypeError:
        raise ValueError("Os operandos devem ser números.")


