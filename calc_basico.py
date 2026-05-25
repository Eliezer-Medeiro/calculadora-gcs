# calc_basico.py

#Módulo A - Operações básicas

#Autor: João Eliézer

#Branch: feature/operacoes_basicas


def somar(a, b):
    try:
        return a + b
    except TypeError:
        raise ValueError("Os operandos devem ser números.")

def subtrair(a, b):
    try:
        return a - b
    except TypeError:
        raise ValueError("Os operandos devem ser números.")

def multiplicar(a, b):
    try:
        return a * b
    except TypeError:
        raise ValueError("Os operandos devem ser números.")

def dividir(a, b):
    try:
        if b == 0:
            raise ValueError("O denominador não pode ser zero.")
        return a / b
    except TypeError:
        raise ValueError("Os operandos devem ser números.")