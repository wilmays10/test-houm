#!/bin/bash

# entorno virtual
sudo apt update
sudo apt install python3-pip
python -m venv env
source env/bin/activate

# instalar dependencias
pip3 install -r requirements.txt

# libreria para soporte geoespacial
sudo apt-get install libsqlite3-mod-spatialite

# Creacion base de datos
python manage.py makemigrations tracking
python manage.py migrate

# Carga de datos de ejemplo
python manage.py loaddata init_data/db.json

# Inicializar server local
python manage.runserver