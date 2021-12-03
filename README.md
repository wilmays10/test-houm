# Test-Houm

Servicio Rest que realiza lo siguiente:
- Retorna las coordenadas de un Houmer.
- Retorna las coordenadas de las propiedades que visitó y cuánto tiempo se
quedó en cada una.
- Retorna todos los momentos en que el houmer se trasladó con una velocidad
superior a cierto parámetro.


Instalación en entorno local:

Tienes que tener instalado pip3 en tu distribución linux. Con pip3 instalado:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    $ sudo pip3 install virtualenv
    $ python -m venv <path ambiente py3>
    $ source <path ambiente py3>/bin/activate
    $ python --version
    Python 3.x
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ya está instalado un ambiente para python3. Ahora debes clonar el
software usando git e instalar dependencias:


    $ git clone https://gitlab.com/wilmays10/test-moni
    $ cd test-moni
    $ pip install -r requirements.txt

-mkdir env_test
- instalar virtualenv
- python3 -m venv env_test
- activar entorno
- check python3
instalacion de librerias geo
- sudo apt-get install libsqlite3-mod-spatialite
crear superusuario