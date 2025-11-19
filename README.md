# FP1 - Teoría - Ejercicios del Tema 5

## Ejercicio 1: Eliminar duplicados de una lista conservando el orden

Implementa una función `elimina_duplicados` en `conjuntos.py` que reciba una lista y devuelva la lista resultante de eliminar los elementos duplicados, conservando para el resto de elementos el orden de la lista original. Usa un conjunto para almacenar los elementos que ya han aparecido.

Por ejemplo, para la lista `[1, 4, 1, 3, 4, 5]` devolvería `[1, 4, 3, 5]`.

Prueba la función mediante la función de test de `conjuntos_test.py`. 

## Ejercicio 2: Unión de múltiples conjuntos

Implementa una función `une_conjuntos` en `conjuntos.py` que reciba una lista de conjuntos y devuelva el conjunto resultante de la unión de todos los conjuntos de la lista.

Prueba la función mediante la función de test de `conjuntos_test.py`. 

## Ejercicio 3: Intersección de múltiples conjuntos

Implementa una función `intersecta_conjuntos` en `conjuntos.py` que reciba una lista de conjuntos y devuelva el conjunto resultante de la intersección de todos los conjuntos de la lista. Es decir, el conjunto resultante contendrá únicamente los elementos comunes a todos los conjuntos de la lista.

Prueba la función mediante la función de test de `conjuntos_test.py`. 

## Ejercicio 4: Sustituye palabras en texto

Implementa una función `sustituye_palabras` en `diccionarios.py` que reciba un texto y un diccionario de tipo `dict[str, str]`, y devuelva el resultado de sustituir en el texto recibido las palabras que aparecen en el diccionario como claves por sus valores asociados.

Por ejemplo, si el texto de entrada es `"hola amigo que estoy muy cansado"` y el diccionario de sustituciones es `{"hola": "holi", "amigo": "amigui",  "que": "k",  "estoy": "toy", "muy": "tela de"}`, el texto devuelto será `"holi amigui k toy tela de cansado"`.

Para simplificar, considera que las palabras siempre están separadas por espacios y no es necesario realizar ninguna limpieza (ni pasar a minúsculas, ni quitar signos de puntuación).

Prueba la función mediante la función de test de `diccionarios_test.py`. 

## Ejercicio 5: Indexa por iniciales

Implementa una función `indexa_por_iniciales` que reciba un texto y devuelva un diccionario de tipo `dict[str, set[str]]` que indexa las distintas palabras del texto por sus iniciales. La función convertirá siempre el texto recibido a minúsculas antes de construir el diccionario.

Por ejemplo, si el texto de entrada es `"Tres tristes tigres comen trigo en un trigal"`, el diccionario resultante será:
```python
    {
        't': {'tres', 'tristes', 'tigres', 'trigo', 'trigal'},
        'c': {'comen'},
        'e': {'en'},
        'u': {'un'}
    }
```

## Ejercicio 6: Detección de idioma

Queremos implementar un detector de idioma de textos (español, inglés y francés). Para ello, nos basaremos en las diferentes distribuciones de letras de cada idioma. Vamos a seguir estos pasos:

* Contaremos el número de apariciones de las distintas **parejas de letras consecutivas (bigramas)** que aparecen en un texto largo de cada uno de los idiomas. Guardaremos estas frecuencias normalizadas de 0 a 1 en un diccionario por cada idioma. Por ejemplo, este es un trozo del diccionario de frecuencias para el francés:
    ```python
    {
        'pd': 1.002194806626512e-05, 'py': 0.00035076818231927925, 'ww': 0.00016035116906024192, 
        'pg': 2.004389613253024e-05, 'np': 2.004389613253024e-05, 'ws': 0.00010021948066265121, 
        'yw': 1.002194806626512e-05, 'hs': 3.0065844198795363e-05, 'ii': 2.004389613253024e-05, ...
    }
    ``` 
* Para decidir si un texto es de un idioma o de otro, calcularemos un diccionario de frecuencias similar al anterior para dicho texto, y lo compararemos con los diccionarios de frecuencias de cada idioma. Decidiremos el idioma del texto en función de la distancia media entre las frecuencias para el texto de entrada y cada uno de los idiomas.

Implementa las siguientes funciones en `diccionarios.py`, y ejecuta las pruebas contenidas en `diccionarios_test.py`.

### Función `construye_frecuencias_bigramas`

Recibe un texto y construye un diccionario de tipo `dict[str, float]` con las frecuencias normalizadas de cada bigrama en el texto dado, ignorando mayúsculas y minúsculas. Un bigrama es una secuencia de dos letras consecutivas en el texto.

Para implementar esta función, primero recorre los caracteres del texto de dos en dos, concaténalos para obtener birgramas, y cuenta las apariciones de cada uno de ellos. Sólo contaremos aquellos bigramas que estén formados por letras. Una vez realizado el conteo, para obtener el diccionario de frecuencias, divide cada recuento por el total de bigramas incluidos en el recuento. 

### Función `calcula_distancia_media_frecuencias`

Calcula la distancia media entre las frecuencias normalizadas representadas por dos diccionarios de frecuencias como los devueltos por la función anterior.

Para implementar esta función, recorre cada una de las claves de ambos diccionarios (puedes crear un conjunto con todas las claves), y suma el valor absoluto de la diferencia entre los recuentos de ambos diccionarios. Por último, divide la suma entre el total de claves para obtener la media. Ten en cuenta que si los diccionarios recibidos estuviesen vacíos, la función debe devolver 0.

### Función `identifica_idioma`

Identifica el idioma de un texto comparando sus frecuencias de bigramas con las frecuencias de bigramas de textos de ejemplo en distintos idiomas.

Además del texto cuyo idioma queremos identificar, la función recibe un diccionario en el que las claves son identificadores de idiomas (por ejemplo, `'es'`, `'en'` y `'fr'`), y los valores son textos largos de esos idiomas. 

Sigue estos pasos:
* Construye el diccionario de frecuencias de bigramas del texto a identificar.
* Para cada pareja `idioma, texto_ejemplo`, construye el diccionario de frecuencias del texto de ejemplo, y calcula la distancia entre este diccionario y el de frecuencias del texto a identificar. Almacena una tupla `(distancia, idioma)` en una lista.
* Calcula la tupla menor de la lista y devuelve el idioma correspondiente a dicha tupla.

## Ejercicio 7

Vamos a trabajar con un fichero CSV real del proyecto *Palmer Penguins*, que contiene información sobre individuos de distintas especies de pingüinos en la Antártida. El objetivo del ejercicio es practicar la lectura de datos y el uso de diccionarios para agrupar y calcular estadísticas.

En el módulo `pingüinos.py` Se proporciona una `namedtuple` llamada `Penguin`, así como una función `lee_pingüinos` que lee el CSV y devuelve una lista de tuplas Penguin, una por cada pingüino del archivo.

Implementa las siguientes funciones y ejecuta las pruebas incluidas en `pingüinos_test.py`.

### Función `cuenta_pingüinos_por_especie`

Construye un diccionario en el que las claves son las distintas especies de pingüino y el valor asociado son recuentos de los individuos de cada especie.

### Función `calcula_media_masa_corporal_por_especie`

Calcula la media de la masa corporal (campo `body_mass_g`) para cada especie de pingüino. Ignora aquellos pingüinos cuyo valor `body_mass_g` sea `None`. Devuelve un diccionario de tipo `dict[str, float]` donde cada clave es una especie y cada valor es su masa media.

### Función `calcula_minimo_maximo_pico_por_especie`

Calcula la longitud mínima y máxima del pico (campo `bill_length_mm`) para cada especie. Ignora aquellos pingüinos cuyo valor `bill_length_mm` sea `None`. Devuelve un diccionario de tipo `dict[str, tuple[float, float]]`, donde las tuplas contienen el mínimo y el máximo, en ese orden.

### Ejercicio extra

Implementa nuevas versiones de cada una de las funciones anteriores, añadiendo un nuevo parámetro `filtra_isla` de tipo `str`, con valor por defecto `None`, que permita filtrar sólo los pingüinos de la isla indicada. Si el parámetro toma el valor `None`, no se realizará ningún filtrado (es decir, el resultado se calculará usando todos los pingüinos de la lista recibida).

