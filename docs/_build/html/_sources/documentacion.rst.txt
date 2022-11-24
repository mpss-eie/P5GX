Documentación
=============

Este proyecto incluye la creación una página web con documentación, creada con ayuda de Sphinx.

Algunos cambios esenciales:

- En ``docs/conf.py`` modificar ``html_title = 'P5GX'`` con el nombre apropiado del grupo.
- En ``docs/index.rst`` colocar el número de grupo y los nombres de las personas integrantes.

Docstrings de NumPy
-------------------

El siguiente es un ejemplo mínimo del formato para este proyecto. La `documentación <https://numpydoc.readthedocs.io/en/latest/format.html>`_ de la guía de estilo de NumPy detalla todas las posibilidades.

.. code:: python

    def funcion():
        """Descripción corta de la función.

        Descripción más larga de la función, donde explica
        su propósito y cualquier otra información relevante.
        Esta descripción puede (y debe) incluir también las
        ecuaciones matemáticas que sean pertinentes para 
        la función, con el formato rST:

        .. math:: f_X(x) = \lambda e^{-\lambda x}

        Parameters
        ----------
        x : int
            Descripción del parámetro.
        y : int
            Descripción del parámetro.

        Returns
        -------
        z : int
            Descripción de la respuesta.
        
        Examples
        --------
        >>> cadena.analisis.parametros(lambd, nu)
        omega_i = 0.2 + 0.019*i
        p_i = 0.2 / (0.2 + 0.019*i)
        q_i = 0.019*i / (0.2 + 0.019*i)

        Valor numérico para un estado i específico:

        >>> cadena.analisis.parametros(lambd, nu, i)
        omega = 0.36
        p = 0.3
        q = 0.7
        """
        z = x + y
        return z

Documentación con Sphinx
------------------------

Estos son los pasos mínimos para crear una documentación con Sphinx a partir de un paquete que ha sido debidamente documentado con *docstrings*. En este caso será creada una página web, pero también es posible generar archivos PDF con LaTeX, ePub y otros.

.. note:: Estos pasos ya fueron realizados en el repositorio, así que no es necesario repetirlos, excepto la instalación o actualización de Sphinx.

- Instalar Sphinx

.. code:: bash

    pip install --upgrade sphinx

- Crear la estructura de archivos

.. code:: bash

    sphinx-quickstart

- Instalar el tema de Sphinx llamado Furo (o cualquier otro de su elección, según los `temas de Sphinx <https://sphinx-themes.org/>`_) con:

.. code:: bash

    pip install furo

- Modificar el archivo ``conf.py``

.. code-block:: python

    import os
    import sys
    sys.path.insert(0, os.path.abspath('..'))
    ...
    extensions = [
        'sphinx.ext.autodoc',
        'sphinx.ext.viewcode',
        'sphinx.ext.napoleon',
        'sphinx.ext.mathjax',
        'myst_parser',
    ]
    ...
    myst_enable_extensions = [
        "amsmath",
        "dollarmath",
        'colon_fence',
    ]
    ...
    language = 'es'
    ...
    html_title = 'P5GX'
    html_theme = 'furo'

.. important:: Para actualizar la página con los últimos cambios:

    .. code:: bash

        $ docs/: make clean html

reStructuredText
----------------

Sphinx utiliza reStructuredText (**rST**) y Markdown para dar formato al texto de la página web. Markdown ya es conocido anteriormente, entonces aquí solamente hay algunas referencias sobre rST.

.. note:: Para utilizar Markdown, es posible consultar la `referencia <https://myst-parser.readthedocs.io/en/latest/syntax/syntax.html>`_ de MyST (*Markedly Structured Text*), el convertidor de Markdown a rST para Sphinx.

Según Docutils:

    reStructuredText es texto sin formato que utiliza construcciones simples e intuitivas para indicar la estructura de un documento. Estas construcciones son igualmente fáciles de leer en forma cruda, plana o procesada como HTML.

La documentación de `Docutils <https://docutils.sourceforge.io/>`_ ofrece una explicación amplia sobre su uso, específicamente la `sección <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html>`_ sobre "reStructuredText Markup Specification" donde está la sintaxis para hacer listas, secciones, tablas, citas, etc. También Sphinx ofrece la `sintaxis básica <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_.

Algunos aspectos esenciales:

- Tiene listas.
- Tiene *cursivas* y **negritas**.
- La indentación es importante.
- Tiene citas textuales (solamente haciendo la indentación):

    En un lugar de La Mancha, de cuyo nombre no quiero acordarme...

- Tiene listas de definición:
    aguacate
        Verde por fuera, verde por dentro y con una semilla de aguacate en el centro.
    piña
        Tiene corona pero no es rey, tiene escamas pero no es pez, tiene ojos pero no ve.

- Tiene fragmentos de código:

.. code-block:: python
    :linenos:
    :emphasize-lines: 3

    import numpy as np

    numero = np.random.randint(0, 10)
    print(numero)

- Tiene imágenes:

.. image:: campana.jpg
    :width: 250
