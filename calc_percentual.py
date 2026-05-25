# calc_percentual.py

#Módulo C - Percentual

#Autor: João Eliézer

#Branch: feature/operacoes_percentual

def percentual(pct, valor):
    try:
        return (pct / 100) * valor
    except TypeError:
        raise ValueError("Os operandos devem ser números.")

def acrescimo(pct, valor):
    try:
        return valor + percentual(pct, valor)
    except TypeError:
        raise ValueError("Os operandos devem ser números.")

def desconto(pct, valor):
    try:
        return valor - percentual(pct, valor)
    except TypeError:
        raise ValueError("Os operandos devem ser números.")


