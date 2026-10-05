# calc_conversao.py

#Módulo E - Conversão

#Autor: João Eliézer

#Branch: feature/operacoes_conversao

"""
Este módulo contém funções para realizar conversões de unidades, como temperatura, distância e peso.
"""

"""
Melhorias:
    1. Substituir numeros mágicos por constantes nomeadas para melhorar a legibilidade do código.
    2. Adicionar docstrings a cada função para descrever seu propósito, parâmetros e valor de retorno.
    3. Como cada função possui o mesmo tratamento de exceção, podemos criar uma função auxiliar para validar os operandos e reduzir a duplicação de código.
"""

CELSIUS_PARA_FAHRENHEIT_FATOR = 9 / 5
FAHRENHEIT_OFFSET = 32
MILHAS_PARA_KM = 0.621371
LIBRAS_PARA_KG = 2.20462

def _validate_valor(valor):
    """Valida se o valor é um número. Levanta uma exceção se não for."""
    if isinstance(valor, bool):
        raise ValueError("O valor deve ser um número.")

    if not isinstance(valor, (int, float)):
        raise ValueError("O valor deve ser um número.")



def celsius_para_fahrenheit(celsius):
    """
    Converte Celsius para Fahrenheit.
    
    Args:
        celsius (int ou float): A temperatura em Celsius.
    
    Returns:
        float: A temperatura convertida em Fahrenheit.
    
    Raises:
        ValueError: Se o valor não for um número.
    
    
    """
    _validate_valor(celsius)
    return (celsius * CELSIUS_PARA_FAHRENHEIT_FATOR) + FAHRENHEIT_OFFSET

def km_para_milhas(km):
    """
    Converte quilômetros para milhas.
    
    Args:
        km (int ou float): A distância em quilômetros.
    
    Returns:
        float: A distância convertida em milhas.
    
    Raises:
        ValueError: Se o valor não for um número.
    """
    _validate_valor(km)
    return km * MILHAS_PARA_KM

def kg_para_libras(kg):
    """
    Converte quilogramas para libras.
    
    Args:
        kg (int ou float): A massa em quilogramas.
    
    Returns:
        float: A massa convertida em libras.
    
    Raises:
        ValueError: Se o valor não for um número.
    """
    _validate_valor(kg)
    return kg * LIBRAS_PARA_KG

def km_para_milhas(km):
    """
    Converte quilômetros para milhas.
    
    Args:
        km (int ou float): A distância em quilômetros.
    
    Returns:
        float: A distância convertida em milhas.
    
    Raises:
        ValueError: Se o valor não for um número.
    """
    _validate_valor(km)
    return km * MILHAS_PARA_KM

def kg_para_libras(kg):
    """
    Converte quilogramas para libras.
    
    Args:
        kg (int ou float): A massa em quilogramas.
    
    Returns:
        float: A massa convertida em libras.
    
    Raises:
        ValueError: Se o valor não for um número.
    """
    _validate_valor(kg)
    return kg * LIBRAS_PARA_KG
