# calc_percentual.py

#Módulo C - Percentual

#Autor: João Eliézer

#Branch: feature/operacoes_percentual

"""
Este módulo contém funções para calcular percentual, acréscimo e desconto.
"""

"""
Melhorias:
    1. Adicionar docstrings a cada função para descrever seu propósito, parâmetros e valor de retorno.
    2. Como cada função possui o mesmo tratamento de exceção, podemos criar uma função auxiliar para validar os operandos e reduzir a duplicação de código.
    3. Trocar o uso abreviações por nomes descritivos.
"""

def _validate_operandos(percentual_valor, valor):
    """
    Valida se os operandos são números. Levanta uma exceção se não forem.

    Args:
        percentual_valor (float): O valor percentual.
        valor (float): O valor base.
    
    Raises:
        ValueError: Se algum dos operandos não for um número.
        
    """
    if isinstance(percentual_valor, bool) or isinstance(valor, bool):
        raise ValueError("Os operandos devem ser números.")

    if not isinstance(percentual_valor, (int, float)) or not isinstance(valor, (int, float)):
        raise ValueError("Os operandos devem ser números.")
    
def percentual(percentual_valor, valor):
    """
    Calcula o percentual de um valor.
    
    Args:
        percentual_valor (float): O valor percentual.
        valor (float): O valor base.
    
    Returns:
        float: O resultado do cálculo do percentual.
    
    Raises:
        ValueError: Se os operandos não forem números.
    """

    _validate_operandos(percentual_valor, valor)
    return (percentual_valor / 100) * valor


def acrescimo(percentual_valor, valor):
    """
    Calcula o acréscimo de um valor com base em um percentual.
    
    Args:
        percentual_valor (float): O valor percentual.
        valor (float): O valor base.
    
    Returns:
        float: O resultado do cálculo do acréscimo.
    
    Raises:
        ValueError: Se os operandos não forem números.
    """

    _validate_operandos(percentual_valor, valor)
    return valor + percentual(percentual_valor, valor)


def desconto(percentual_valor, valor):
    """
    Calcula o desconto de um valor com base em um percentual.
    
    Args:
        percentual_valor (float): O valor percentual.
        valor (float): O valor base.
    
    Returns:
        float: O resultado do cálculo do desconto.
    
    Raises:
        ValueError: Se os operandos não forem números.
    """

    _validate_operandos(percentual_valor, valor)
    return valor - percentual(percentual_valor, valor)



