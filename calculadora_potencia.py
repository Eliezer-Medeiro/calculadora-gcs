# calc_potencia.py

#Módulo B - Potência e raízes

#Autor: João Eliézer

#Branch: feature/operacoes_potencia

"""
Este módulo contém funções para calcular potência e raízes quadradas e cúbicas.
"""

"""
Melhorias:
    1. Adicionar docstrings a cada função para descrever seu propósito, parâmetros e valor de retorno.
    2. Como cada função possui o mesmo tratamento de exceção, podemos criar uma função auxiliar para validar os operandos e reduzir a duplicação de código.
    3. Trocar o uso de números mágicos por constantes nomeadas para melhorar a legibilidade do código.
"""



MEIO = 0.5
UM_TERCO = 1/3

def _validate_operandos(base, expoente = 0):
    """
    Valida se os operandos são números. Levanta uma exceção se não forem.

    Args:
        base (float): A base.
        expoente (float): O expoente.
    
    Raises:
        ValueError: Se algum dos operandos não for um número.
    """

    if isinstance(base, bool) or isinstance(expoente, bool):
        raise ValueError("Os operandos devem ser números.")

    if not isinstance(base, (int, float)) or not isinstance(expoente, (int, float)):
        raise ValueError("Os operandos devem ser números.")

def potencia(base, expoente):
    """
    Calcula a potência de um número.

    Args:
        base (float): A base.
        expoente (float): O expoente.

    Returns:
        float: O resultado do cálculo da potência.

    Raises:
        ValueError: Se os operandos não forem números.
    """
    
    _validate_operandos(base, expoente)
    return base ** expoente
    

def raiz_quadrada(numero):
    """
    Calcula a raiz quadrada de um número.

    Args:
        numero (float): O número.

    Returns:
        float: O resultado do cálculo da raiz quadrada.

    Raises:
        ValueError: Se o operando não for um número ou for negativo.
    """

    _validate_operandos(numero)
    if numero < 0:
        raise ValueError("Não é possível calcular a raiz quadrada de um número negativo.")
    return numero ** MEIO

def raiz_cubica(numero):
    """
    Calcula a raiz cúbica de um número.

    Args:
        numero (float): O número.

    Returns:
        float: O resultado do cálculo da raiz cúbica.

    Raises:
        ValueError: Se o operando não for um número.
    """

    _validate_operandos(numero)
    return numero ** UM_TERCO
