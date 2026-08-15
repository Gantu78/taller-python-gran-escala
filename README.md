# Taller de Python — Procesamiento de Datos a Gran Escala

Cuadernos de Jupyter del taller de fundamentos de Python de la asignatura **Procesamiento de Datos a Gran Escala**, Pontificia Universidad Javeriana (Bogotá). Cubren las estructuras de datos y construcciones básicas del lenguaje como base para el trabajo posterior con datos a gran escala.

## Contenido

| Cuaderno | Tema |
|---|---|
| [01-Python-Cadenas.ipynb](01-Python-Cadenas.ipynb) | Cadenas: indexación, slicing, inmutabilidad, métodos de texto y secuencias de escape |
| [02-Python-Tuplas.ipynb](02-Python-Tuplas.ipynb) | Tuplas: creación, indexación, concatenación, anidamiento e inmutabilidad |
| [03-Python-Listas.ipynb](03-Python-Listas.ipynb) | Listas: slicing, `append`/`extend`, `del`, `split()`, alias vs. copia |
| [04-Python-Conjuntos.ipynb](04-Python-Conjuntos.ipynb) | Conjuntos: duplicados, `add`/`remove`, unión, intersección, diferencia |
| [05-Python-Diccionarios.ipynb](05-Python-Diccionarios.ipynb) | Diccionarios: pares clave-valor, `keys()`, `values()`, existencia de claves |
| [06-Python-Condiciones.ipynb](06-Python-Condiciones.ipynb) | Condicionales: comparaciones, `if`/`elif`/`else`, operadores lógicos |
| [07-Python-Bucles.ipynb](07-Python-Bucles.ipynb) | Bucles: `range()`, `for`, `enumerate()`, `while` |
| [08-Python-Funciones.ipynb](08-Python-Funciones.ipynb) | Funciones: `def`, parámetros, docstrings, retorno, alcance de variables |
| [09_Python_Clases.ipynb](09_Python_Clases.ipynb) | Programación orientada a objetos: clases, `__init__`, `self`, instancias |
| [Practico_Bono_1.ipynb](Practico_Bono_1.ipynb) | Ejercicios prácticos de repaso (calentamiento, nivel 1 y nivel 2) |

## Requisitos

- Python 3.11+
- Jupyter (Notebook o JupyterLab)

## Uso

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
jupyter lab
```

Cada cuaderno puede ejecutarse de forma independiente, celda por celda.

## Estructura

- `_backup/` — copias de respaldo de los cuadernos generadas automáticamente.
- `requirements.txt` — dependencias del entorno de Jupyter.

## Autor

Samuel Gantiva — Estudiante de Ingeniería de Sistemas, Pontificia Universidad Javeriana, con énfasis en Inteligencia Artificial y Ciencia de Datos.
