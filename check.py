#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Script de comprobacion de entrega de ejercicio

Para ejecutarlo, desde la shell:
 $ python check.py login_github

"""

import os
import random
import sys

ejercicio = 'X-Serv-14.3-URLsAleatorias'

student_files = [
    'servidor-random-http.py'
    ]

repo_files = [
    'check.py',
    'README.md',
    '.gitignore',
    '.git'
    ]

files = student_files + repo_files

if len(sys.argv) != 2:
    print()
    sys.exit("Usage: $ python check.py login_github")

repo_gitlab = "https://gitlab.etsit.urjc.es/" + sys.argv[1] + "/" + ejercicio


aleatorio = str(int(random.random() * 1000000))

error = 0

print()
print("Clonando el repositorio " + repo_gitlab + "\n")
os.system('git clone ' + repo_gitlab + ' /tmp/' + aleatorio + ' > /dev/null 2>&1')
try:
    gitlab_file_list = os.listdir('/tmp/' + aleatorio)
except OSError:
    error = 1
    print("Error: No se ha podido acceder al repositorio " + repo_gitlab + ".")
    print()
    sys.exit()

if len(gitlab_file_list) != len(files):
    error = 1
    print("Error: numero de ficheros en el repositorio incorrecto")

for filename in files:
    if filename not in gitlab_file_list:
        error = 1
        print("\tError: " + filename + " no encontrado en el repositorio.")

if not error:
    print("Parece que la entrega se ha realizado bien.")

print()
print("La salida de pep8 es: (si todo va bien, no ha de mostrar nada)")
print()
for filename in student_files:
    if filename in gitlab_file_list:
        os.system('pep8 --repeat --show-source --statistics /tmp/'
                  + aleatorio + '/' + filename)
    else:
        print("Fichero " + filename + " no encontrado en el repositorio.")
print()
