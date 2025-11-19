from diccionarios import *

def test_sustituye_palabras():
    print("Probando sustituye_palabras...", end="")

    texto = "hola amigo que estoy muy cansado"
    diccionario = {
        "hola": "holi",
        "amigo": "amigui",
        "que": "k",
        "estoy": "toy",
        "muy": "tela de"
    }
    res = sustituye_palabras(texto, diccionario)
    assert res == "holi amigui k toy tela de cansado"

    texto = "este es un texto de prueba"
    diccionario = {
        "noexiste": "valor"
    }
    res = sustituye_palabras(texto, diccionario)
    assert res == "este es un texto de prueba"

    texto = ""
    diccionario = {
        "hola": "holi"
    }
    res = sustituye_palabras(texto, diccionario)
    assert res == ""

    texto = "palabra palabra palabra"
    diccionario = {
        "palabra": "word"
    }
    res = sustituye_palabras(texto, diccionario)
    assert res == "word word word"

    print(" OK")

def test_indexa_por_iniciales():
    print("Probando indexa_por_iniciales...", end="")

    texto = "Ana ama a Alberto y a Alicia"
    res = indexa_por_iniciales(texto)
    expected = {
        'a': {'ana', 'ama', 'alberto', 'a', 'alicia'},
        'y': {'y'}
    }
    assert res == expected

    texto = ""
    res = indexa_por_iniciales(texto)
    expected = {}
    assert res == expected

    texto = "Hola hola HELLO hello"
    res = indexa_por_iniciales(texto)
    expected = {
        'h': {'hola', 'hello'}
    }
    assert res == expected

    texto = "123 1abc 2def 3ghi"
    res = indexa_por_iniciales(texto)
    expected = {
        '1': {'123', '1abc'},
        '2': {'2def'},
        '3': {'3ghi'}
    }
    assert res == expected

    print(" OK")
    
def test_construye_frecuencias_bigramas():
    print("Probando construye_frecuencias_bigramas...", end="")

    texto = "abab"
    res = construye_frecuencias_bigramas(texto)
    expected = {
        'ab': 0.6666666666666666,
        'ba': 0.3333333333333333
    }
    assert res == expected

    texto = "aaaa"
    res = construye_frecuencias_bigramas(texto)
    expected = {
        'aa': 1.0
    }
    assert res == expected

    texto = ""
    res = construye_frecuencias_bigramas(texto)
    expected = {}
    assert res == expected

    texto = "abcde"
    res = construye_frecuencias_bigramas(texto)
    expected = {
        'ab': 0.25,
        'bc': 0.25,
        'cd': 0.25,
        'de': 0.25
    }
    assert res == expected

    print(" OK")

def test_calcula_distancia_media_frecuencias():
    print("Probando calcula_distancia_media_frecuencias...", end="")

    freq1 = {'a': 0.5, 'b': 0.5}
    freq2 = {'a': 0.5, 'b': 0.5}
    res = calcula_distancia_media_frecuencias(freq1, freq2)
    assert res == 0.0

    freq1 = {'a': 1.0}
    freq2 = {'b': 1.0}
    res = calcula_distancia_media_frecuencias(freq1, freq2)
    assert res == 1.0

    freq1 = {}
    freq2 = {}
    res = calcula_distancia_media_frecuencias(freq1, freq2)
    assert res == 0.0

    freq1 = {'a': 0.7, 'b': 0.3}
    freq2 = {'a': 0.4, 'b': 0.6}
    res = calcula_distancia_media_frecuencias(freq1, freq2)
    assert res - 0.3 < 1e-9

    print(" OK")

def test_identifica_idioma():
    # Primero cargamos los archivos en.txt, es.txt y fr.txt que están en la carpeta data
    print("Probando identifica_idioma...")
    textos_ejemplo = {}
    idiomas = ['en', 'es', 'fr']
    for idioma in idiomas:
        with open(f"data/{idioma}.txt", "r", encoding="utf-8") as f:
            textos_ejemplo[idioma] = f.read()
    
    texto_a_identificar = """There was nothing so _very_ remarkable in that; nor did Alice think it
so _very_ much out of the way to hear the Rabbit say to itself, “Oh
dear! Oh dear! I shall be late!” (when she thought it over afterwards,
it occurred to her that she ought to have wondered at this, but at the
time it all seemed quite natural); but when the Rabbit actually _took a
watch out of its waistcoat-pocket_, and looked at it, and then hurried
on, Alice started to her feet, for it flashed across her mind that she
had never before seen a rabbit with either a waistcoat-pocket, or a
watch to take out of it, and burning with curiosity, she ran across the
field after it, and fortunately was just in time to see it pop down a
large rabbit-hole under the hedge."""
    res = identifica_idioma(textos_ejemplo, texto_a_identificar)
    print(f"\tIdentificando texto: {texto_a_identificar[:60]}...")
    print(f"\tIdioma identificado: {res}")
    assert res == "en"

    texto_a_identificar = """No sé hasta qué punto sea lícito hacer uso de confidencias vertidas
en el seno de la más íntima amistad y llevar al público opiniones o
apreciaciones que no las destinaba a él quien las profiriera. Y Goti
ha cometido en su prólogo la indiscreción de publicar juicios míos
que nunca tuve intención de que se hiciesen públicos. O por lo menos
nunca quise que se publicaran con la crudeza con que en privado los
exponía."""
    res = identifica_idioma(textos_ejemplo, texto_a_identificar)
    print(f"\tIdentificando texto: {texto_a_identificar[:60]}...")
    print(f"\tIdioma identificado: {res}")
    assert res == "es"

    texto_a_identificar = """Sur la rive sud du fleuve Saint-Laurent, dans une plaine qui s'étend
jusqu'à une chaîne de montagnes, dont nous ignorons le nom, se trouve
une petite chaumière qui n'a rien de remarquable par elle-même;
située au bas d'une colline, sa vue est dérobée aux voyageurs par un
bosquet de pins qui la défend contre le vent du nord, si fréquent
dans cette partie de la contrée. Autrefois cette misérable cabane
était habitée par trois personnes: un homme, son épouse, jeune femme
vieillie par le chagrin, et un enfant, fruit de leur union. Cet homme
que nous appellerons Charles Amand la possédait au temps dont nous
parlons; en ayant éloigné ses autres habitants afin de vaquer
secrètement à des travaux mystérieux auxquels il avait dévoué sa vie.
C'était le 15 août de l'année 182-."""
    res = identifica_idioma(textos_ejemplo, texto_a_identificar)
    print(f"\tIdentificando texto: {texto_a_identificar[:60]}...")
    print(f"\tIdioma identificado: {res}")
    assert res == "fr"

test_sustituye_palabras()
#test_indexa_por_iniciales()
#test_construye_frecuencias_bigramas()
#test_calcula_distancia_media_frecuencias()
#test_identifica_idioma()
print("Todos los tests pasaron correctamente.")