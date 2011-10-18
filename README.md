
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
                Append C:\Python27

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

Clone this Django project, then run it

    git clone git@github.com:victorneo/osstwitter-oct19.git
    cd osstwitter-oct19
    python manage.py runserver

Navigate to http://localhost:8000/.
