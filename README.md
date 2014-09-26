dj_mundo_cooperativo
====================


### Instalación


    git clone git@github.com:banquito/dj_mundo_cooperativo.git
    virtualenv ENV
    source ENV/bin/activate
    cd dj_mundo_cooperativo
    pip install -r requirements.txt
    cd mc
    python manage.py migrate
    python manage.py runserver

En el navegador:

    http://localhost:8000
