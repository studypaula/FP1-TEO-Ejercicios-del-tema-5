from conjuntos import *

def test_elimina_duplicados():
    print("Probando elimina_duplicados...", end="")

    lista = [1, 4, 1, 3, 4, 5]
    res =  elimina_duplicados(lista)
    assert res == [1, 4, 3, 5]

    lista = ['a', 'b', 'a', 'c', 'b']
    res = elimina_duplicados(lista)
    assert res == ['a', 'b', 'c']

    lista = [1, 2, 3, 4, 5]
    res = elimina_duplicados(lista)
    assert res == [1, 2, 3, 4, 5]

    lista = []
    res = elimina_duplicados(lista)
    assert res == []

    lista = [1, 1, 1, 1]
    res = elimina_duplicados(lista)
    assert res == [1]
    
    print(" OK")

def test_une_conjuntos():
    print("Probando une_conjuntos...", end="")

    lista_de_conjuntos = [{1, 2}, {2, 3}, {3, 4}]
    res = une_conjuntos(lista_de_conjuntos)
    assert res == {1, 2, 3, 4}

    lista_de_conjuntos = [set(), {1, 2}, {2, 3}]
    res = une_conjuntos(lista_de_conjuntos)
    assert res == {1, 2, 3}

    lista_de_conjuntos = []
    res = une_conjuntos(lista_de_conjuntos)
    assert res == set()

    lista_de_conjuntos = [{1, 2}, {1, 2}, {1, 2}]
    res = une_conjuntos(lista_de_conjuntos)
    assert res == {1, 2}

    print(" OK")

def test_intersecta_conjuntos():
    print("Probando intersecta_conjuntos...", end="")

    lista_de_conjuntos = [{1, 2, 3}, {2, 3, 4}, {3, 2}]
    res = intersecta_conjuntos(lista_de_conjuntos)
    assert res == {2, 3}

    lista_de_conjuntos = [set(), {1, 2}, {2, 3}]
    res = intersecta_conjuntos(lista_de_conjuntos)
    assert res == set()

    lista_de_conjuntos = []
    res = intersecta_conjuntos(lista_de_conjuntos)
    assert res == set()

    lista_de_conjuntos = [{1, 2}, {1, 2}, {1, 2}]
    res = intersecta_conjuntos(lista_de_conjuntos)
    assert res == {1, 2}

    print(" OK")

test_elimina_duplicados()
test_une_conjuntos()
test_intersecta_conjuntos()
print("Todos los tests pasaron correctamente.")