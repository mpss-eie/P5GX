# Creación del paquete

Esta es la referencia para la creación e instalación de un paquete de Python.

## Estructura de directorios y archivos

```
P5GX/
├─ setup.py
├─ clientes.csv
├─ cadena/
│  ├─ __init__.py
│  ├─ analisis.py
│  ├─ simulacion.py
│  ├─ servicio.py
│  ├─ dimensionamiento.py
├─ README.md
├─ docs/
├─ revision.py
├─ P5.ipynb
├─ .gitignore
```

- `setup.py` tiene metadatos del paquete, incluyendo autores y dependencias de otros paquetes.
- `cadena/` es un directorio con los módulos del paquete.
    - `__init__.py` es requerido para importar el directorio como un paquete y debe estar vacío.
    - `*.py` son los archivos donde están las funciones de cada módulo.
- `README.md` tiene documentación básica y los resultados del proyecto (visible para quien visita el repositorio en GitHub).
- `docs/` tiene los archivos de la documentación generada con Sphinx.
- `revision.py` es el archivo utilizado para revisar la funcionalidad del proyecto.
- `P5.ipynb` es el enunciado del proyecto y está aquí solamente como referencia.
- `.gitignore` tiene los archivos, directorios o extensiones que son ignorados al hacer confirmaciones (*commits*) con Git, generalmente porque se trata de archivos de uso local que no deben ser compartidos con el repositorio.

## Requisitos previos

1. Actualizar `pip` (*Package Installer for Python*):

```bash
$ python -m pip install --upgrade pip
```

2. Instalar librerías para creación de paquetes:

```bash
$ pip install setuptools
$ pip install wheel
```

- `setuptools` es para descargar, compilar, instalar, actualizar y desinstalar paquetes de Python.
- `wheel` es una extensión de `setuptools` que crea archivos WHL (Wheel) para distribución de paquetes que contienen todos los archivos y metadatos necesarios para la instalación en la computadora.

## Creación del paquete

> Ejecutar en la interfaz de línea de comandos de su computadora, en el mismo directorio donde está el repositorio local del proyecto.

**Nota**: puede navegar los directorios de su computadora con el comando `cd` (*change directory*). Ejemplo: `$ cd /Users/maria/Documentos/MPSS/Proyecto5/P5G17` (cambia según el sistema operativo).

1. Creación de los archivos WHL (Wheel): 

```bash
$ python setup.py bdist_wheel
```

Esto creará varios directorios nuevos: `build`, `dist` y `cadena.egg-info`, con los que `pip` hace la instalación en el paso siguiente.

2. Instalación local del paquete con `pip`:

```bash
$ pip install /ubicacion/del/directorio/del/proyecto
```

**Nota**: puede encontrar `/ubicacion/del/directorio/del/proyecto` con el comando `pwd` (*print working directory*). O bien, si ya está en ese directorio, basta con hacer:

```bash
$ pip install .
```

donde `.` significa el directorio actual. Si todo resulta bien, saldrá algo como:

```bash
Successfully installed cadena-0.0.1
```

3. Verificación de la instalación (revisar que está en la lista de paquetes instalados).

```bash
$ pip list
```

Ahora el paquete `cadena` está disponible para ser utilizado localmente en cualquier programa de Python, importando sus módulos, por ejemplo:

```python
from cadena import analisis, simulacion, servicio, dimensionamiento

analisis.parametros()
...
```

## Revisión del proyecto

- **Funcionalidad**: la revisión de la funcionalidad debe estar en el archivo `revision.py`. Este archivo es una demostración del proyecto y debe ser editado por el grupo para mostrar los resultados apropiados según el desarrollo de cada función y las decisiones tomadas en cuanto a sus argumentos de entrada. 
- **PEP-8**: la revisión será hecha, para cada módulo, con:
```bash
$ pycodestyle --ignore=E226 paquete/modulo.py
```
Los códigos de error de `pycodestyle` están disponibles en su [documentación](https://pycodestyle.pycqa.org/en/latest/intro.html#error-codes).
- **Docstrings**: la revisión será hecha con:
```bash
$ pydocstyle paquete/modulo.py
```
Los códigos de error de `pydocstyle` están disponibles en su [documentación](https://www.pydocstyle.org/en/stable/error_codes.html).

Por favor hacer estas revisiones antes y corregir los errores de formato que ahí sean indicados.

:::{important}
Una correcta documentación con *dosctrings* es necesaria para que Sphinx construya apropiadamente la página web de documentación.
:::

## Referencias

Para conocer más sobre la creación de paquetes en Python:

- [How to create a Python library](https://medium.com/analytics-vidhya/how-to-create-a-python-library-7d5aea80cc3f)
- [Packaging Python Projects](https://packaging.python.org/en/latest/tutorials/packaging-projects/)
- [Setuptools Quickstart](https://setuptools.pypa.io/en/latest/userguide/quickstart.html)
