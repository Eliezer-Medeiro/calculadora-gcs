def menu():
    print("===Calculadora GCS ===\n")

    try:
        from calc_basico import somar, subtrair, multiplicar, dividir

        print("Módulo Basico carregado.")
        print(" 3 + 3 =", somar(3, 3))
        print(" 3 - 3 =", subtrair(3, 3))
        print(" 3 x 3 =", multiplicar(3, 3))
        print(" 3 / 3 =", dividir(3, 3))
    except ImportError:
        print("Módulo Básico ainda não disponível.")
    
    try:
        from calc_potencia import potencia, raiz_quadrada, raiz_cubica
        print("Módulo Potência carregado.")
        print(" 3³ =", potencia(3, 3))
        print("sqrt(9) = ", raiz_quadrada(9))
        print("raiz cubica de 27 = ", raiz_cubica(27))
    except ImportError:
        print("Módulo Potência ainda não disponível.")
    
    try:
        from calc_percentual import percentual, acrescimo, desconto
        print("Módulo Potência ainda não disponível.")
        print("15'%' de 100 =", percentual(15, 100))
        print("Acrescimo de 50% no valor de 100 é = ", acrescimo(50, 100))
        print("Desconto de 2% no valor de 20 é =", desconto(2, 20))

    except ImportError:
        print("Módulo Potência ainda não disponível.")

    try:
        from calc_estatistica import media, mediana, desvio_padrao
        print("Módulo Estatistica carregado.")
        lista = [10, 11, 3, 65, 70, 32, 43, 55, 9, 18]
        print("Media da Lista = ", media(lista))
        print("Mediana da Lista = ", mediana(lista))
        print("Desvio padrao da Lista =", desvio_padrao(lista))
    except ImportError:
        print("Módulo Estatistica ainda não disponível.")
    
    try:
        from calc_conversao import celsius_para_fahrenheit, km_para_milhas, kg_para_libras
        print("Módulo Conversão carregado.")
        print("30°C para °F = ", celsius_para_fahrenheit(30))
        print("100km para milhas =", km_para_milhas(100))
        print("10kg para libras =", kg_para_libras(10))

    except ImportError:
        print("Módulo Conversão ainda não disponível.")

if __name__ == "__main__":
    menu()

