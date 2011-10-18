
## Git & Python workshop 19th October


### Installation

Start by installing Git and Python for those who do not have them
installed.

    Git = latest stable
    Python >= 2.6 (Do NOT get Python 3.x)

    Windows:
        Git: http://git-scm.com
        Python: http://python.org (install to default directory, then
                set PATH)
                Append 

    OS X:
        Git: brew install git # for homebrew
        Python: Already installed

    *nix:
        Use your package manager, eg. Ubuntu
        sudo apt-get install git python

        For source installation, get it from the websites above.

Test out Git and Python installation
    git --version
    python
    print('Hello World!')
    exit() # or CTRL + d

### Django

Next, install Django.

    easy_install django

Create a Django project, then run it

    django-admin.py startproject osstwitter
    cd osstwitter
    python manage.py runserver

Request everyone to navigate to http://localhost:8000/ to view the
temporary Django page.

Once, open up 'settings.py' to discuss about the settings.

    First, talk about DEBUG = True
        It's a variable assignment
        Python boolean variables are True or False

    Talk about ADMINS tuple
        There are lists and tuples in Python
        Easy to be confused
        a_list = ['hello', 'world']
        a_tuple = ('hello', 'world')

        a_list[0]
        a_tuple[0]

        a_list.append('earthlings')
        a_tuple.append('earthlings') # ERROR


    Talk about Dictionaries, similar to hash tables in Java
        classrooms = {} # dict()
        classrooms[1] = 50
        classrooms['Lab 9'] = 30

    Database:
        sqlite3
        osstwitter.sqlite
