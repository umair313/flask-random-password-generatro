
# Random Password Generator web app using flask

## Project directory tree
```
tree

|   .gitignore
|   Procfile
|   Readme.md
|   requirements.txt
|   wsgi.py
|
\---app
    |   main.py
    |
    +---static
    |       style.css
    |
    \---templates
            index.html
```

## Requirements
- click==8.0.3
- colorama==0.4.4
- Flask==2.0.2
- gunicorn==20.1.0
- itsdangerous==2.0.1
- Jinja2==3.0.2
- MarkupSafe==2.0.1
- Werkzeug==2.0.2

## How to Run the application
``python wsgi.py``

## Want to deploy on Heroku?
 if your want to deply on heruko and you are not using ``python-3.9.7`` then create a file ``runtime.txt``
 by default it will use ``python-3.9.7``
 
 ### readme.txt
 ```
python-(your python version here remove pranthises)
 ```
 