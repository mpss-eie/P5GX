Datos de análisis
=================

.. note::
    Este es el tipo de datos que utiliza el paquete como fuente para hacer sus análisis.

Esta tabla especifica el tiempo de llegada (en segundos desde el inicio de la simulación) de los primeros  𝑁  clientes de un sistema, el intervalo de tiempo (segundos) entre el cliente y el anterior y la duración del servicio (segundos) prestado a cada uno. Nótese que no está especificado el tiempo en que son atendidos, únicamente el tiempo de la llegada, ya que el momento de la atención es variable: puede suceder antes o después, dependiendo de la fila en el sistema.

+----------+----------+------------+-----------+
| cliente  | llegada  | intervalo  | servicio  |
+==========+==========+============+===========+
| 1        | 8        | 8          | 67        |
+----------+----------+------------+-----------+
| 2        | 10       | 2          | 12        |
+----------+----------+------------+-----------+
| 3        | 17       | 7          | 3         |
+----------+----------+------------+-----------+
| 4        | 18       | 1          | 12        |
+----------+----------+------------+-----------+
| 5        | 53       | 35         | 66        |
+----------+----------+------------+-----------+
| 6        | 62       | 9          | 7         |
+----------+----------+------------+-----------+
| 7        | 83       | 21         | 21        |
+----------+----------+------------+-----------+
| 8        | 92       | 9          | 16        |
+----------+----------+------------+-----------+
| 9        | 127      | 35         | 8         |
+----------+----------+------------+-----------+
| 10       | 149      | 22         | 5         |
+----------+----------+------------+-----------+
| ...      | ...      | ...        | ...       |
+----------+----------+------------+-----------+
