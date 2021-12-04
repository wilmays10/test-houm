# Test-Houm

Servicio Rest que realiza lo siguiente:
- Retorna las coordenadas de un Houmer.
- Retorna las coordenadas de las propiedades que visitó y cuánto tiempo se
quedó en cada una.
- Retorna todos los momentos en que el houmer se trasladó con una velocidad
superior a cierto parámetro.

# Tecnología usada

Desarrollado sobre Django 3.2.9 + Python3. Utiliza una base de datos Sqlite con soporte geoespacial 'spatiallite'. Incluye también DjangoRestFramework para el desarrollo de las API's.



Instalación en entorno local:
Clonar el repositorio y posicionarse en el directorio descargado
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    $ git clone https://github.com/wilmays10/test-houm
    $ cd test-houm
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Dar permiso de ejecución al script de inicio.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    $ chmod +x init_local.sh
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ejecutar el scrip 'init_local.sh'
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    $ ./init_local.sh
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Consideraciones

- Los datos geográficos de las propiedades se guardarán en la base de datos como poligonos. Dependiendo del uso que se le quiera dar, tal vez alcance con guardar un sólo punto representativo de la propiedad.
- La velocidad es un valor que se podría calcular entre los tiempos de dos
ubicaciones diferentes. En este caso se asume que es un valor que nos brinda el GPS para no tener que calcularlo. Además, por simplicidad,se guarda en un campo de tipo entero.
