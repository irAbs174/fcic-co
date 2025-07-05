#!/bin/bash

echo "Start Auto builder and production exposer ...";

#python3 -m venv env
source env/bin/activate

#pip3 install --upgrade pip
#pip3 install -r requirements.txt

clear
python3 manage.py check

clear
python3 manage.py runserver