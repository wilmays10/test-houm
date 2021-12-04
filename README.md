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

Ejecutar el scrip 'init_local.sh'
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    $ ./init_local.sh
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Consideraciones

- Los datos geográficos de las propiedades se guardarán en la base de datos como poligonos. Dependiendo del uso que se le quiera dar, tal vez alcance con guardar un sólo punto representativo de la propiedad.
- La velocidad es un valor que se podría calcular entre los tiempos de dos
ubicaciones diferentes. En este caso se asume que es un valor que nos brinda el GPS para no tener que calcularlo. Además, por simplicidad,se guarda en un campo de tipo entero.

# API's

Una vez que esté ejecutandosé el servidor local, se puede acceder a las API's:

http://localhost:8000/

# Coordenadas de un Houmer:
http://localhost:8000/trackings/

Parámetro obligatorio:
- id: id del houmer seleccionado.

Se debe pasar por método GET el id de algún houmer, por ejemplo:
http://localhost:8000/trackings/?id=1

# Coordenadas de las propiedades que visitó y cuanto tiempo se quedó en cada una:
http://localhost:8000/properties/

En este caso, los parámetros obligatorios son:
- date: fecha elegida con formato 'dd-mm-AAAA'
- id_houmer: id del houmer seleccionado.

Ejemplo:
http://localhost:8000/properties/?id_houmer=1&date=04-12-2021

# Momentos en que el houmer se trasladó con una velocidad superior a cierto parámetro:
http://localhost:8000/velocities/

Parámetros obligatorios:
- date: fecha elegida con formato 'dd-mm-AAAA'
- id_houmer: id del houmer seleccionado.
- param: valor base de la velocidad. Se retorna los momentos mayores o iguales a param.

Ejemplo:
http://localhost:8000/velocities/?id_houmer=1&date=4-12-2021&param=10
