# calc_potencia.py

#Módulo B - Potência e raízes

#Autor: João Eliézer

#Branch: feature/operacoes_basicas

def potencia(base, expoente):
    try:
        return base ** expoente
    except TypeError:
        raise ValueError("Os operandos devem ser números.")

def raiz_quadrada(numero):
    try:
        if numero < 0:
            raise ValueError("Não é possível calcular a raiz quadrada de um número negativo.")
        return numero ** 0.5
    except TypeError:
        raise ValueError("O operando deve ser um número.")

def raiz_cubica(numero):
    try:
        return numero ** (1/3)
    except TypeError:
        raise ValueError("O operando deve ser um número.")
