from pingüinos import *

def test_cuenta_pingüinos_por_especie():
    print("Probando cuenta_pingüinos_por_especie...")

    pingüinos = lee_pingüinos("data/penguins.csv")

    res = cuenta_pingüinos_por_especie(pingüinos)
    print(f"\t Resultado: {res}")
    expected = {'Adelie': 152, 'Gentoo': 124, 'Chinstrap': 68}
    assert res == expected

def test_calcula_media_masa_corporal_por_especie():
    print("Probando calcula_media_masa_corporal_por_especie...")

    pingüinos = lee_pingüinos("data/penguins.csv")

    res = calcula_media_masa_corporal_por_especie(pingüinos)
    print(f"\t Resultado: {res}")
    expected = {'Adelie': 3700, 'Gentoo': 5076, 'Chinstrap': 3733}
    assert res == expected

def test_calcula_minimo_maximo_pico_por_especie():
    print("Probando calcula_minimo_maximo_pico_por_especie...")

    pingüinos = lee_pingüinos("data/penguins.csv")

    res = calcula_minimo_maximo_pico_por_especie(pingüinos)
    print(f"\t Resultado: {res}")
    expected =  {'Adelie': (32.1, 46.0), 'Gentoo': (40.9, 59.6), 'Chinstrap': (40.9, 58.0)}
    assert res == expected

def test_cuenta_pingüinos_por_especie_filtro():
    print("Probando cuenta_pingüinos_por_especie con filtro...")

    pingüinos = lee_pingüinos("data/penguins.csv")

    res = cuenta_pingüinos_por_especie_filtro(pingüinos, filtra_isla="Biscoe")
    print(f"\t Resultado: {res}")
    expected = {'Gentoo': 124, 'Adelie': 44}
    assert res == expected

def test_calcula_media_masa_corporal_por_especie_filtro():
    print("Probando calcula_media_masa_corporal_por_especie con filtro...")

    pingüinos = lee_pingüinos("data/penguins.csv")

    res = calcula_media_masa_corporal_por_especie_filtro(pingüinos, filtra_isla="Biscoe")
    print(f"\t Resultado: {res}")
    expected = {'Adelie': 3709, 'Gentoo': 5076}
    assert res == expected

def test_calcula_minimo_maximo_pico_por_especie_filtro():
    print("Probando calcula_minimo_maximo_pico_por_especie con filtro...")

    pingüinos = lee_pingüinos("data/penguins.csv")

    res = calcula_minimo_maximo_pico_por_especie_filtro(pingüinos, filtra_isla="Biscoe")
    print(f"\t Resultado: {res}")
    expected =  {'Adelie': (34.5, 45.6), 'Gentoo': (40.9, 59.6)}
    assert res == expected

test_cuenta_pingüinos_por_especie()
#test_calcula_media_masa_corporal_por_especie()
#test_calcula_minimo_maximo_pico_por_especie()
#test_cuenta_pingüinos_por_especie_filtro()
#test_calcula_media_masa_corporal_por_especie_filtro()
#test_calcula_minimo_maximo_pico_por_especie_filtro()
print("Todos los tests pasaron correctamente.")