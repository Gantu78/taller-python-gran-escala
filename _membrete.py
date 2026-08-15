# -*- coding: utf-8 -*-
"""
Agrega el membrete de identificacion y la seccion de Conclusiones
a los cuadernos del taller. No toca ninguna celda de ejercicios.

Si ya existe una seccion de Conclusiones (de una corrida anterior),
la reemplaza por la version definitiva.

Uso:  python _membrete.py
"""

import json
import shutil
from pathlib import Path

BASE = Path(__file__).parent
BACKUP = BASE / "_backup"

AUTOR = (
    "**Descripción del autor:** Estudiante de Ingeniería de Sistemas de la "
    "Pontificia Universidad Javeriana (Bogotá), con énfasis en Inteligencia "
    "Artificial y Ciencia de Datos. Interés en el análisis de datos y el "
    "desarrollo de software aplicado."
)

MEMBRETE = """---

# Procesamiento de Datos a Gran Escala
### Taller de Python — Lab 01

| | |
|---|---|
| **Nombre completo** | Samuel Gantiva |
| **Documento de identidad** | C.C. 1.011.322.519 |
| **Asignatura** | Procesamiento de Datos a Gran Escala |
| **Fecha** | 14 de agosto de 2026 |

{autor}

**Contenido de este cuaderno:** {contenido}

---"""

MARCA = "## Conclusiones"

PLANTILLA_CONCLUSIONES = """---

## Conclusiones

{cuerpo}
"""

NOTEBOOKS = {

    "01-Python-Cadenas.ipynb": {
        "contenido": None,  # ya tiene membrete propio; no se sobrescribe
        "conclusiones": """- **Una cadena es una secuencia ordenada.** Cada carácter ocupa una posición que empieza en 0, y la indexación negativa permite llegar al final sin necesidad de conocer la longitud previamente.
- **El slicing tiene el límite superior exclusivo.** `Name[0:4]` devuelve cuatro caracteres, no cinco. Es un detalle pequeño pero es la fuente de error más común al extraer subcadenas.
- **Las cadenas son inmutables.** Métodos como `upper()` o `replace()` no modifican la cadena original: construyen una nueva y la devuelven. Si el resultado no se asigna a una variable, el cambio se pierde.
- **`find()` no lanza error cuando falla.** Devuelve `-1`, así que ese valor debe validarse antes de usarlo como índice; de lo contrario se termina accediendo al último carácter sin darse cuenta.
- **Las secuencias de escape resuelven lo que no se puede escribir directamente.** `\\n`, `\\t` y `\\\\` insertan salto de línea, tabulación y barra invertida; el prefijo `r` desactiva esa interpretación y muestra la cadena tal cual.

En el contexto de la asignatura, buena parte del trabajo previo al análisis consiste en limpiar texto: unificar mayúsculas, corregir separadores, localizar patrones. Las operaciones vistas aquí son la base de esa limpieza, y se aplican con la misma lógica cuando el volumen pasa de una cadena a millones de registros.""",
    },

    "02-Python-Tuplas.ipynb": {
        "contenido": "Tuplas en Python: creación, tipos mixtos, indexación positiva y negativa, concatenación, slicing, anidamiento, inmutabilidad y ordenamiento con `sorted()`.",
        "conclusiones": """- **La tupla es una secuencia ordenada e inmutable.** Comparte con las cadenas la indexación, el slicing y la concatenación, pero admite elementos de tipos distintos dentro de la misma estructura.
- **Intentar modificar un elemento produce un `TypeError`.** No existe forma de reasignar una posición: para obtener una tupla distinta hay que construir una nueva, normalmente por concatenación.
- **`sorted()` devuelve una lista, no una tupla.** Esto es coherente con la inmutabilidad, y conviene tenerlo presente porque el tipo del resultado cambia respecto al de entrada.
- **Las tuplas se pueden anidar.** El acceso a los niveles internos se hace encadenando índices, y resulta útil pensar la estructura como un árbol para no perderse en los niveles.
- **La inmutabilidad es una garantía, no una limitación.** Asegura que un registro no se altere por accidente y permite que una tupla funcione como clave de un diccionario, cosa que una lista no puede hacer.

Las tuplas encajan bien cuando se representan registros que no deberían cambiar: coordenadas, una fila de resultados, un par de valores asociados. Al procesar datos, usarlas en esos casos comunica la intención de que el dato es fijo.""",
    },

    "03-Python-Listas.ipynb": {
        "contenido": "Listas en Python: indexación, slicing, stride, modificación de elementos, métodos `append` y `extend`, eliminación con `del`, conversión desde cadenas con `split()` y diferencia entre alias y copia.",
        "conclusiones": """- **La lista es la contraparte mutable de la tupla.** Mantiene el orden y la indexación, pero permite modificar, agregar y eliminar elementos después de creada.
- **`append` y `extend` no hacen lo mismo.** `append` añade un único elemento (si es una lista, queda anidada), mientras que `extend` incorpora cada elemento por separado. Confundirlos cambia la estructura del resultado.
- **Los métodos que modifican en el sitio devuelven `None`.** Escribir `A = A.append(x)` deja la variable en `None` y borra la lista. Conviene llamarlos como sentencia, no como expresión.
- **Asignar no es copiar.** `B = A` crea un alias: ambas variables apuntan al mismo objeto y los cambios se reflejan en las dos. Para obtener una copia independiente hay que usar `B = A[:]`. Este es el error más difícil de rastrear del cuaderno, porque no produce ningún mensaje de error.
- **`split()` conecta el mundo del texto con el de las listas.** Permite convertir una línea con separadores en una colección manipulable, que es exactamente el primer paso al leer un archivo delimitado.

La lista es la estructura de trabajo por defecto en Python. Entender cuándo se está pasando una referencia y cuándo una copia es fundamental en cuanto los datos empiezan a circular entre funciones.""",
    },

    "04-Python-Conjuntos.ipynb": {
        "contenido": "Conjuntos en Python: creación a partir de listas, eliminación automática de duplicados, métodos `add`, `remove` y verificación con `in`, y operaciones lógicas de intersección, unión, diferencia, subconjunto y superconjunto.",
        "conclusiones": """- **Un conjunto es una colección de elementos únicos.** Convertir una lista con `set()` elimina los duplicados en una sola instrucción, sin necesidad de recorrerla ni comparar elemento por elemento.
- **No hay orden ni índices.** No se puede acceder por posición y el orden en que se imprimen los elementos no corresponde al de inserción. Si el orden importa, el conjunto no es la estructura adecuada.
- **Las operaciones lógicas traducen directamente la teoría de conjuntos.** `&` para intersección, `union()` para unión, `difference()` para diferencia, junto con `issubset()` e `issuperset()`. La representación con diagramas de Venn del cuaderno ayuda a fijar cuál usar en cada caso.
- **La diferencia no es simétrica.** `A.difference(B)` y `B.difference(A)` devuelven resultados distintos, algo evidente en el diagrama pero fácil de invertir al escribir el código.
- **Verificar pertenencia con `in` es la operación más eficiente del conjunto.** A diferencia de la lista, no requiere recorrer los elementos, lo que se vuelve relevante cuando la colección es grande.

Deduplicar registros y comparar colecciones son tareas constantes al integrar varias fuentes de datos. El conjunto las resuelve de manera directa y con mejor rendimiento que hacerlo manualmente sobre listas.""",
    },

    "05-Python-Diccionarios.ipynb": {
        "contenido": "Diccionarios en Python: estructura de pares clave-valor, acceso por clave, adición y eliminación de entradas, verificación de existencia y consulta con `keys()` y `values()`.",
        "conclusiones": """- **La clave reemplaza al índice.** A diferencia de listas y tuplas, el acceso no depende de la posición sino de una etiqueta significativa, lo que hace el código mucho más legible.
- **Las claves deben ser únicas e inmutables.** Sirven cadenas, números o tuplas, pero no listas. Si se asigna un valor a una clave existente, se sobrescribe en lugar de crear una entrada nueva.
- **`in` consulta claves, no valores.** Es una diferencia importante frente a listas y conjuntos, y explica por qué buscar un valor requiere recorrer `values()` explícitamente.
- **`keys()` y `values()` permiten separar la estructura del contenido.** Resultan útiles para recorrer el diccionario o para verificar qué campos están presentes antes de procesarlo.
- **El acceso por clave es directo.** No implica recorrer la estructura, lo que mantiene el costo estable aunque el diccionario crezca.

De todas las colecciones vistas, el diccionario es la más parecida a un registro real: las respuestas de una API, los documentos JSON y las filas de una base de datos se corresponden casi uno a uno con esta estructura. Es también la base sobre la que se construye un `DataFrame` en pandas.""",
    },

    "06-Python-Condiciones.ipynb": {
        "contenido": "Estructuras condicionales: operadores de comparación, evaluación de expresiones booleanas, sentencias `if`, `else` y `elif`, y combinación de condiciones con los operadores lógicos `and`, `or` y `not`.",
        "conclusiones": """- **Las comparaciones producen valores booleanos.** El resultado de `a == b` es un dato como cualquier otro: se puede guardar en una variable, imprimir o combinar, lo cual ayuda a depurar condiciones complejas evaluándolas por partes.
- **`==` compara y `=` asigna.** Es la confusión más frecuente al empezar, y en Python produce un error de sintaxis dentro de un `if`, lo que al menos facilita detectarla.
- **El orden de las ramas determina el resultado.** Un `if`/`elif`/`else` evalúa de arriba hacia abajo y ejecuta únicamente la primera condición verdadera. Si una condición general se ubica antes que una específica, la segunda nunca se alcanza.
- **`and` exige que todas las condiciones se cumplan; `or` basta con una.** Combinarlos permite expresar reglas complejas en una sola línea, aunque conviene usar paréntesis para dejar clara la precedencia.
- **La indentación define el bloque.** No hay llaves ni palabras de cierre: un espacio de más o de menos cambia qué instrucciones pertenecen a la condición y, por tanto, la lógica del programa.

El control de flujo es lo que convierte una secuencia de instrucciones en un programa capaz de decidir. Al trabajar con datos se traduce directamente en filtros, reglas de validación y clasificación de registros.""",
    },

    "07-Python-Bucles.ipynb": {
        "contenido": "Bucles en Python: generación de secuencias con `range()`, iteración con `for` sobre listas y colecciones, uso de `enumerate()` y ciclos `while` controlados por condición.",
        "conclusiones": """- **`range()` genera la secuencia sobre la que se itera.** Con un solo argumento arranca en 0, y el límite superior siempre es exclusivo: `range(3)` produce 0, 1 y 2.
- **`for` y `while` responden a situaciones distintas.** El primero se usa cuando se conoce de antemano la colección o el número de repeticiones; el segundo, cuando la repetición depende de una condición que puede cambiar durante la ejecución.
- **Iterar sobre los elementos es más claro que iterar sobre índices.** Recorrer directamente la lista evita el manejo manual de posiciones y reduce los errores por salirse del rango.
- **`enumerate()` entrega índice y elemento al mismo tiempo.** Resuelve el caso en que se necesitan ambos sin tener que llevar un contador aparte.
- **Un `while` mal planteado no termina.** Si la condición no cambia dentro del cuerpo del ciclo, el programa queda ejecutándose indefinidamente. Conviene verificar siempre qué instrucción hará que la condición deje de cumplirse.

Los bucles son el mecanismo básico de repetición, pero también el punto donde aparece el costo cuando el volumen crece: recorrer millones de elementos uno por uno en Python es lento. Precisamente por eso las librerías orientadas a datos, como NumPy o pandas, ofrecen operaciones vectorizadas que evitan el ciclo explícito.""",
    },

    "08-Python-Funciones.ipynb": {
        "contenido": "Funciones en Python: definición con `def`, parámetros y argumentos, documentación con docstrings, valores de retorno, alcance de variables, argumentos por defecto y funciones integradas como `len`, `sum` y `sorted`.",
        "conclusiones": """- **Una función encapsula un bloque reutilizable.** Se define una vez y se invoca cuantas veces sea necesario, lo que reduce la repetición y concentra los cambios en un solo lugar.
- **Sin `return` explícito, la función devuelve `None`.** Es un comportamiento silencioso: el programa no falla, simplemente el valor esperado no aparece, y suele descubrirse más adelante en el flujo.
- **El docstring es documentación ejecutable.** Escrito justo debajo del `def`, queda disponible mediante `help()`, y encaja con la exigencia del taller de documentar lo que se implementa.
- **El alcance de las variables separa lo interno de lo externo.** Las variables locales dejan de existir al terminar la función; las globales son visibles desde dentro, pero modificarlas requiere `global` y conviene evitarlo porque vuelve difícil rastrear de dónde viene un valor.
- **`sorted()` y `sort()` no son intercambiables.** El primero devuelve una lista nueva y deja la original intacta; el segundo ordena en el sitio y devuelve `None`. La distinción entre operaciones que copian y operaciones que modifican vuelve a aparecer aquí.

Modularizar en funciones facilita probar cada pieza por separado y sustituirla sin romper el resto. En un flujo de procesamiento de datos, cada etapa —cargar, limpiar, transformar, resumir— se expresa naturalmente como una función independiente.""",
    },

    "09_Python_Clases.ipynb": {
        "contenido": "Programación orientada a objetos: definición de clases, atributos y métodos, constructor `__init__`, uso de `self`, creación de instancias, inspección con `dir()` y ejemplos gráficos con Matplotlib.",
        "conclusiones": """- **La clase es una plantilla; el objeto es la instancia concreta.** La clase describe qué datos y qué comportamiento tendrán los objetos, pero solo al instanciarla se reserva espacio con valores propios.
- **`__init__` se ejecuta automáticamente al crear el objeto.** Es el lugar donde se inicializan los atributos, y explica por qué los argumentos se pasan al llamar la clase y no al método.
- **`self` es la referencia al objeto sobre el que se trabaja.** Aparece como primer parámetro de cada método, aunque no se pasa al invocarlo, y es lo que permite que dos instancias de la misma clase mantengan valores independientes.
- **Los métodos actúan sobre el estado del objeto.** A diferencia de una función suelta, no necesitan recibir los datos como argumento: los toman de los atributos de la propia instancia.
- **`dir()` permite inspeccionar un objeto en ejecución.** Lista sus atributos y métodos disponibles, lo que resulta práctico al explorar clases de librerías que no se conocen.

La programación orientada a objetos ordena el código cuando los datos y las operaciones que actúan sobre ellos van juntos. En el ámbito de la asignatura, encaja bien para representar, por ejemplo, un conjunto de datos con métodos propios para cargarlo, validarlo y resumirlo, en lugar de dispersar esa lógica en funciones sueltas.""",
    },

    "Practico_Bono_1.ipynb": {
        "contenido": "Ejercicios prácticos de repaso organizados en tres niveles (calentamiento, nivel 1 y nivel 2), que integran condicionales, operaciones con cadenas, listas y definición de funciones.",
        "conclusiones": """- **Casi ningún ejercicio se resuelve con un solo concepto.** La mayoría exige combinar condicionales con operaciones sobre cadenas o listas dentro de una función, que es justamente lo que diferencia este cuaderno de los anteriores.
- **El operador módulo resuelve las verificaciones de paridad.** `lesser_of_two_evens` y `makes_twenty` se apoyan en `%` junto con condiciones combinadas; el reto está en traducir correctamente el enunciado, no en la sintaxis.
- **La inmutabilidad de las cadenas vuelve a ser determinante.** En `old_macdonald` y `paper_doll` no se puede modificar un carácter en su lugar: hay que construir una cadena nueva por concatenación o slicing.
- **`split()` y `join()` funcionan como operaciones inversas.** `master_yoda` lo muestra con claridad: se separa la oración en palabras, se invierte la lista y se vuelve a unir en una sola cadena.
- **Recorrer pares consecutivos exige cuidado con el rango.** En `has_33` hay que comparar cada elemento con el siguiente sin salirse de la lista, lo que obliga a detener el ciclo un paso antes del final.
- **El orden de evaluación cambia el resultado.** En `blackjack`, el ajuste por el once debe aplicarse antes de la comprobación final; invertir esos pasos produce respuestas incorrectas en los casos límite.

El bloque práctico confirma que la dificultad real no está en recordar la sintaxis, sino en descomponer un enunciado en pasos y elegir la estructura adecuada para cada uno. Escribir primero los casos de prueba, tal como vienen en el enunciado, resultó la forma más rápida de verificar cada solución.""",
    },
}


def md(texto):
    """Construye una celda markdown en formato nbformat."""
    lineas = texto.split("\n")
    fuente = [l + "\n" for l in lineas[:-1]] + [lineas[-1]]
    return {"cell_type": "markdown", "metadata": {}, "source": fuente}


def texto_celda(celda):
    src = celda.get("source", "")
    return src if isinstance(src, str) else "".join(src)


def main():
    BACKUP.mkdir(exist_ok=True)
    resumen = []

    for nombre, datos in NOTEBOOKS.items():
        ruta = BASE / nombre
        if not ruta.exists():
            resumen.append("[!] No encontrado: " + nombre)
            continue

        shutil.copy2(ruta, BACKUP / nombre)

        with ruta.open(encoding="utf-8") as f:
            nb = json.load(f)

        celdas = nb.get("cells", [])
        acciones = []

        # --- Membrete ---
        idx = next(
            (i for i, c in enumerate(celdas)
             if "Documento de identidad" in texto_celda(c)),
            None,
        )

        if idx is None:
            celdas.insert(0, md(MEMBRETE.format(
                autor=AUTOR, contenido=datos["contenido"])))
            acciones.append("membrete agregado")
        else:
            actual = texto_celda(celdas[idx])
            if "Descripción del autor" not in actual:
                celdas[idx] = md(actual.replace(
                    "**Contenido de este cuaderno:**",
                    AUTOR + "\n\n**Contenido de este cuaderno:**",
                    1,
                ))
                acciones.append("descripción del autor agregada")
            else:
                acciones.append("membrete ya completo")

        # --- Conclusiones (reemplaza cualquier version previa) ---
        previas = [i for i, c in enumerate(celdas) if MARCA in texto_celda(c)]
        for i in reversed(previas):
            celdas.pop(i)

        celdas.append(md(PLANTILLA_CONCLUSIONES.format(
            cuerpo=datos["conclusiones"])))
        acciones.append(
            "conclusiones reemplazadas" if previas else "conclusiones agregadas")

        nb["cells"] = celdas
        with ruta.open("w", encoding="utf-8") as f:
            json.dump(nb, f, indent=1, ensure_ascii=False)
            f.write("\n")

        resumen.append("[ok] " + nombre + ": " + ", ".join(acciones))

    print("\n".join(resumen))
    print("\nCopias de seguridad en: " + str(BACKUP))


if __name__ == "__main__":
    main()
