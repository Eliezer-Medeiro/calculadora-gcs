def menu():
    print("===Calculadora GCS ===\n")

    try:
        from calc_basico import somar, subtrair, multiplicar, dividir

        print("Módulo Basico carregado.")
        print(f" 3 + 3 = {somar(3, 3)}")
        print(f" 3 - 3 = {subtrair(3, 3)}")
        print(f" 3 x 3 = {multiplicar(3, 3)}")
        print(f" 3 / 3 = {dividir(3, 3):.2f}")
    except ImportError:
        print("Módulo Básico ainda não disponível.")
    
    try:
        from calc_potencia import potencia, raiz_quadrada, raiz_cubica
        print("\nMódulo Potência carregado.")
        print(f" 3³ = {potencia(3, 3):.0f}")
        print(f"sqrt(9) = {raiz_quadrada(9):.0f}")
        print(f"raiz cubica de 27 = {raiz_cubica(27):.0f}")
    except ImportError:
        print("Módulo Potência ainda não disponível.")
    
    try:
        from calc_percentual import percentual, acrescimo, desconto
        print("\nMódulo Percentual carregado.")
        print(f"15'%' de 100 = {percentual(15, 100):.2f}")
        print(f"Acrescimo de 50% no valor de 100 é = {acrescimo(50, 100):.2f}")
        print(f"Desconto de 2% no valor de 20 é = {desconto(2, 20):.2f}")

    except ImportError:
        print("Módulo Percentual ainda não disponível.")

    try:
        from calc_estatistica import media, mediana, desvio_padrao
        print("\nMódulo Estatistica carregado.")
        lista = [10, 11, 3, 65, 70, 32, 43, 55, 9, 18]
        print(f"Media da Lista = {media(lista):.2f}")
        print(f"Mediana da Lista = {mediana(lista):.2f}")
        print(f"Desvio padrao da Lista = {desvio_padrao(lista):.2f}")
    except ImportError:
        print("Módulo Estatistica ainda não disponível.")
    
    try:
        from calc_conversao import celsius_para_fahrenheit, km_para_milhas, kg_para_libras
        print("\nMódulo Conversão carregado.")
        print(f"30°C para °F = {celsius_para_fahrenheit(30):.2f}")
        print(f"100km para milhas = {km_para_milhas(100):.2f}")
        print(f"10kg para libras = {kg_para_libras(10):.2f}")

    except ImportError:
        print("Módulo Conversão ainda não disponível.")

if __name__ == "__main__":
    menu()

