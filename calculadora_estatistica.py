# calc_estatistica.py

#Módulo D - Estatística

#Autor: João Eliézer

#Branch: feature/operacoes_estatistica

"""
Este módulo contém funções para realizar cálculos estatísticos, como média, mediana e desvio padrão.
"""

"""
Melhorias:
    1. Adicionar docstrings a cada função para descrever seu propósito, parâmetros e valor de retorno.
    2. Como cada função possui o mesmo tratamento de exceção, podemos criar uma função auxiliar para validar os operandos e se a lista estiver vazia, afim de reduzir a duplicação de código.
    3. Trocar o uso de caracteres por nomes descritivos.
"""
EXPOENTE_RAIZ_QUADRADA = 0.5

def _validate_lista(lista):
    """Valida se a lista não está vazia e se contém apenas números. Levanta uma exceção se não for."""
    
    if not lista:
        raise ValueError("A lista não pode estar vazia.")

    if isinstance(lista, bool):
        raise ValueError("A lista deve conter apenas números.")
    
    if not all(isinstance(x, (int, float)) for x in lista):
        raise ValueError("A lista deve conter apenas números.")

def media(lista):
    """
    Calcula a média de uma lista de números.
    
    Args:
        lista (list): Uma lista de números.
    
    Returns:
        float: A média dos números na lista.
    
    Raises:
        ValueError: Se a lista estiver vazia ou contiver elementos que não sejam números.
    """

    _validate_lista(lista)
    try:
        return sum(lista) / len(lista)
    except TypeError:
        raise ValueError("A lista deve conter apenas números.")
    except Exception as e:
        raise RuntimeError(f"Ocorreu um erro inesperado: {e}")

def mediana(lista):
    """
    Calcula a mediana de uma lista de números.
    
    Args:
        lista (list): Uma lista de números.
    
    Returns:
        float: A mediana dos números na lista.
    
    Raises:
        ValueError: Se a lista estiver vazia ou contiver elementos que não sejam números.
    """

    _validate_lista(lista)
    lista_ordenada = sorted(lista)
    tamanho_lista = len(lista_ordenada)
    meio = tamanho_lista // 2

    if tamanho_lista % 2 == 0:
        return (lista_ordenada[meio - 1] + lista_ordenada[meio]) / 2
    else:
        return lista_ordenada[meio]
    
    
def desvio_padrao(lista):
    """
    Calcula o desvio padrão de uma lista de números.
    
    Args:
        lista (list): Uma lista de números.
    
    Returns:
        float: O desvio padrão dos números na lista.
    
    Raises:
        ValueError: Se a lista estiver vazia ou contiver elementos que não sejam números.
    """
    _validate_lista(lista)
    valor_media = media(lista)
    variancia = sum((x - valor_media) ** 2 for x in lista) / len(lista)
    return variancia ** EXPOENTE_RAIZ_QUADRADA


