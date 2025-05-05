#! /usr/bin/bash

 
export FLASK_APP=runApp.py
export PYTHONPATH=$(pwd)

export DB_NAME=bookiverse
export DB_URL=localhost
export DB_USER=root
export DB_PWD=kashif
export DB_PORT=3306

 
python3 runApp.py