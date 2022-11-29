# Proyecto

Este es el enunciado del proyecto, como referencia.

## `P5` - *Teoría de colas*

> Este es un ejercicio con los conceptos de las cadenas de Markov y los procesos de nacimiento y muerte, utilizando las herramientas de programación y cálculo numérico de Python. El proyecto tiene un paradigma de programación funcional y crea un paquete de Python por medio del trabajo colaborativo con Git, y además genera documentación automática del proyecto.

## Procesos de nacimiento y muerte

Los procesos de nacimiento y muerte son un caso especial de las cadenas de Markov donde las transiciones solamente pueden ocurrir de un estado $i$ a un estado $i + 1$ ("nacimiento" o llegada) o $i - 1$ ("muerte" o salida). 

- Las llegadas están modeladas con un parámetro $\lambda$ de una corriente de Poisson, parámetro también llamado "intensidad". $\lambda$ tiene unidades "personas/minuto" o "solicitudes/segundo", etc. y refleja la distribución exponencial que describe el tiempo aleatorio de llegada entre un "cliente" y otro.
- Las salidas, o tiempo de servicio, están modeladas exponencialmente con un parámetro $\nu$. También $\nu$ es el parámetro de una distribución exponencial que modela la duración del "servicio" para cada "cliente".

Dos componentes dentro de estos sistemas son aleatorios:

- El **tiempo** que tarda "la máquina" (el sistema) en el estado $i$, que está modelado exponencialmente con un parámetro $\Omega_i$.
- La **transición** que hará de ese estado, que puede ser "hacia arriba" ($i+1$) con probabilidad $p_i$ o "hacia abajo" ($i-1$) con probabilidad $q_i$.

Es necesario encontrar la expresión para $\Omega_i$, $p_i$ y $q_i$ en términos de $\lambda$ y $\nu$ para conocer la dinámica del sistema.

## Problema

Es necesario dimensionar la capacidad de un sistema con base en la previsión de solicitudes recibidas ("clientes") por segundo y bajo ciertos parámetros de calidad del servicio.

El archivo adjunto `clientes.csv` especifica el tiempo de llegada (en segundos desde el inicio de la simulación) de los primeros $N$ clientes de un sistema, el intervalo de tiempo (segundos) entre el cliente y el anterior y la duración del servicio (segundos) prestado a cada uno. Nótese que no está especificado el tiempo en que son atendidos, únicamente el tiempo de la llegada, ya que el momento de la atención es variable: puede suceder antes o después, dependiendo de la fila en el sistema.

Este archivo será utilizado para obtener los parámetros iniciales.

### Objetivos

> Sea un proceso modelado como un sistema M/M/1, donde la entrada de clientes es una corriente de Poisson con parámetro $\lambda$ y el nodo de servicio está modelado con un parámetro $\nu$.

En primer lugar, es necesario realizar un estudio de la intensidad de las solicitudes al sistema, para encontrar el parámetro $\lambda$.

En segundo lugar, es necesario realizar un estudio del tiempo de servicio a cada solicitud, para encontrar el parámetro $\nu$.

Seguidamente, es posible realizar una simulación, el análisis del servicio provisto y el diseño del sistema para satisfacer ciertos parámetros de servicio.

### Asignaciones

- Módulo `analisis`: Este módulo determina los parámetros de los datos un sistema M/M/1.

1. (10 %) Implementar una función `llegada()` capaz de encontrar el parámetro $\lambda$ de la intensidad de llegadas al sistema, modelado como una corriente de Poisson. 
2. (10 %) Implementar una función `servicio()` capaz de encontrar el parámetro $\nu$ del tiempo de servicio del sistema.
3. (10 %) Implementar una función `parametros()` capaz de encontrar los parámetros $\Omega_i$, $p_i$ y $q_i$ del sistema para cada estado.

- Módulo `simulacion`: Este módulo simula y visualiza un sistema M/M/1 con parámetros dados.

4. (10 %) Implementar una función `sistema()` capaz de simular una secuencia de llegadas y salidas de clientes al sistema, según los parámetros encontrados. 
5. (10 %) Implementar una función `visualizacion()` capaz de crear una gráfica para observar un ejemplo del comportamiento del sistema con los parámetros encontrados $\lambda$ y $\nu$. 

- Módulo `servicio`: Este módulo analiza la probabilidad de estado estable de cada estado -es decir, el número de personas en el sistema- y determina el porcentaje del tiempo que la fila del sistema está por encima de cierto valor en un sistema M/M/1.

6. (10 %) Implementar una función `probabilidad()` capaz de determinar el vector de estado estable para cada estado.
7. (10 %) Implementar una función `fila()` capaz de determinar el porcentaje de clientes que hacen una fila de $L_q$ espacios antes de recibir el servicio.

- Módulo `dimensionamiento`: Este módulo permite el diseño del número de servidores $s$ en un sistema M/M/s y también el parámetro de servicio $\nu$ necesario para satisfacer cierto criterio de servicio.

8. (10 %) Implementar una función `servidores()` capaz de encontrar el número de servidores necesarios para satisfacer un parámetro dado de calidad del servicio. 
9. (10 %) Implementar una función `tiempo()` capaz de encontrar el tiempo promedio del servicio necesario para satisfacer un parámetro dado de calidad del servicio.

**Nota**: El criterio de "calidad del servicio" utilizado aquí es el siguiente: dado un porcentaje del tiempo, $P$, si el sistema tiene más de una cantidad $L_q$ de clientes en fila por una fracción de tiempo menor a $P$ entonces no satisface el criterio. Por ejemplo, es deseado que no exista una fila de más de 5 clientes el 95% del tiempo. Si se analiza el sistema por un periodo de tiempo de 10 minutos y durante un minuto la fila fue de 6 clientes o más, entonces no fue satisfecho el criterio, puesto que solamente el 90% del tiempo fue cumplida la condición, y se requería el 95%.

Ambas funciones deben recibir parámetros $L_q$ y $P$ arbitrarios para encontrar el número de servidores $s$ en `servidores()` y $\nu$ en `tiempo()` de forma que satisfaga la condición, si es posible.

- Documentación

10. (10 %) Todas las funciones deben estar documentadas con una página web generada por Sphinx.


## Programación del proyecto

Este es un proyecto de programación funcional (basado en funciones), de la misma forma que los proyectos 3 y 4. El propósito es también crear un paquete de Python que será llamado `cadena`, y será desarrollado de forma colaborativa con Git y GitHub. Este paquete tiene varios módulos, cuyas funciones están descritas en los módulos: `analisis`, `simulacion`, `servicio` y `dimensionamiento`.

Cada grupo tiene un repositorio con la siguiente estructura de directorios y archivos:

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

> La revisión del proyecto se hará con el código de `revision.py`, que utiliza todas las funciones solicitadas.

