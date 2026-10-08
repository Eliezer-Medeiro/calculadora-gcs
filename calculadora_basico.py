# calc_basico.py

#Módulo A - Operações básicas

#Autor: João Eliézer

#Branch: feature/operacoes_basicas

"""
Este módulo contém funções para realizar operações matemáticas básicas, como soma, subtração, multiplicação e divisão. 
Cada função recebe dois argumentos numéricos e retorna o resultado da operação correspondente. Caso os argumentos não 
sejam números ou, no caso da divisão, se o denominador for zero, uma exceção será levantada com uma mensagem de erro apropriada.
"""

"""
Melhorias:
    1. Como cada função possui o mesmo tratamento de exceção, podemos criar uma função auxiliar para validar os operandos e reduzir a duplicação de código.
    2 . renomear as variáveis para nomes mais descritivos, como 'operando1' e 'operando2', para melhorar a legibilidade do código.
    3. Adicionar docstrings a cada função para descrever seu propósito, parâmetros e valor de retorno.
"""

def _validate_operandos(operando1, operando2):
    """Valida se os operandos são números. Levanta uma exceção se não forem."""
    if isinstance(operando1, bool) or isinstance(operando2, bool):
        raise ValueError("Os operandos devem ser números.")

    if not isinstance(operando1, (int, float)) or not isinstance(operando2, (int, float)):
        raise ValueError("Os operandos devem ser números.")


def somar(operando1, operando2):
    """
    Somar dois números.
    
    Args:
        operando1 (int ou float): O primeiro número.
        operando2 (int ou float): O segundo número.
    Returns:
        int ou float: A soma dos dois números.
    Raises:
        ValueError: Se algum dos operandos não for um número.
    
    """
    _validate_operandos(operando1, operando2)
    return operando1 + operando2


def subtrair(operando1, operando2):
    """
    Subtrair o segundo número do primeiro.
    
    Args:
        operando1 (int ou float): O primeiro número.
        operando2 (int ou float): O segundo número.
    Returns:
        int ou float: A subtração dos dois números.
    Raises:
        ValueError: Se algum dos operandos não for um número.
    """

    _validate_operandos(operando1, operando2)
    return operando1 - operando2


def multiplicar(operando1, operando2):
    """
    Multiplicar dois números.
    
    Args:
        operando1 (int ou float): O primeiro número.
        operando2 (int ou float): O segundo número.
    Returns:
        int ou float: A multiplicação dos dois números.
    Raises:
        ValueError: Se algum dos operandos não for um número.
    """
    _validate_operandos(operando1, operando2)
    return operando1 * operando2


def dividir(operando1, operando2):
    """
    Dividir o primeiro número pelo segundo.
    
    Args:
        operando1 (int ou float): O primeiro número.
        operando2 (int ou float): O segundo número.
    Returns:
        int ou float: A divisão dos dois números.
    Raises:
        ValueError: Se algum dos operandos não for um número ou se o denominador for zero.
    """
    _validate_operandos(operando1, operando2)
    if operando2 == 0:
        raise ValueError("O denominador não pode ser zero.")
    return operando1 / operando2