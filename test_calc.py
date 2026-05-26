import pytest

from calc_basico import somar, subtrair, multiplicar, dividir
from calc_potencia import potencia, raiz_quadrada, raiz_cubica
from calc_percentual import percentual, acrescimo, desconto
from calc_estatistica import media, mediana, desvio_padrao
from calc_conversao import celsius_para_fahrenheit, km_para_milhas, kg_para_libras

# Testes para o módulo de operações básicas
def test_somar():
    assert somar(3, 3) == 6
    assert somar(-1, 1) == 0
    assert somar(0, 0) == 0

def test_subtrair():
    assert subtrair(3, 3) == 0
    assert subtrair(-1, 1) == -2
    assert subtrair(0, 0) == 0

def test_multiplicar():
    assert multiplicar(3, 3) == 9
    assert multiplicar(-1, 1) == -1
    assert multiplicar(0, 0) == 0

def test_dividir():
    assert dividir(3, 3) == 1
    assert dividir(-1, 1) == -1
    try:
        dividir(1, 0)
    except ValueError as e:
        assert str(e) == "O denominador não pode ser zero."

# Testes para o módulo de potência e raízes
def test_potencia():
    assert potencia(3, 3) == 27
    assert potencia(2, 4) == 16
    assert potencia(5, 0) == 1

def test_raiz_quadrada():
    assert raiz_quadrada(9) == 3
    assert raiz_quadrada(16) == 4
    assert raiz_quadrada(0) == 0

def test_raiz_cubica():
    assert raiz_cubica(27) == pytest.approx(3)
    assert raiz_cubica(64) == pytest.approx(4)
    assert raiz_cubica(0) == 0

# Testes para o módulo de percentual
def test_percentual():
    assert percentual(15, 100) == 15
    assert percentual(50, 200) == 100
    assert percentual(0, 100) == 0

def test_acrescimo():
    assert acrescimo(50, 100) == 150
    assert acrescimo(20, 200) == 240
    assert acrescimo(0, 100) == 100

def test_desconto():
    assert desconto(2, 20) == 19.6
    assert desconto(10, 100) == 90
    assert desconto(0, 100) == 100

# Testes para o módulo de estatística
def test_media():
    assert media([10, 11, 3, 65, 70, 32, 43, 55, 9, 18]) == 31.6
    assert media([1, 2, 3]) == 2
    assert media([0, 0, 0]) == 0

def test_mediana():
    assert mediana([10, 11, 3, 65, 70, 32, 43, 55, 9, 18]) == 25.0
    assert mediana([1, 2, 3]) == 2
    assert mediana([0, 0, 0]) == 0

def test_desvio_padrao():
    assert desvio_padrao([10, 11, 3, 65, 70, 32, 43, 55, 9, 18]) == pytest.approx(23.82, abs=0.01)
    assert desvio_padrao([1, 2, 3]) == pytest.approx(0.816, abs=0.01)
    assert desvio_padrao([0, 0, 0]) == 0

# Testes para o módulo de conversão
def test_celsius_para_fahrenheit():
    assert celsius_para_fahrenheit(30) == 86
    assert celsius_para_fahrenheit(0) == 32
    assert celsius_para_fahrenheit(-40) == -40

def test_km_para_milhas():
    assert km_para_milhas(100) == pytest.approx(62.1371)
    assert km_para_milhas(0) == 0
    assert km_para_milhas(1) == pytest.approx(0.621371)

def test_kg_para_libras():
    assert kg_para_libras(10) == pytest.approx(22.0462)
    assert kg_para_libras(0) == 0
    assert kg_para_libras(1) == pytest.approx(2.20462)

if __name__ == "__main__":
    test_somar()
    test_subtrair()
    test_multiplicar()
    test_dividir()
    test_potencia()
    test_raiz_quadrada()
    test_raiz_cubica()
    test_percentual()
    test_acrescimo()
    test_desconto()
    test_media()
    test_mediana()
    test_desvio_padrao()
    test_celsius_para_fahrenheit()
    test_km_para_milhas()
    test_kg_para_libras()
    print("Todos os testes passaram com sucesso!")
