# Flasky
A trivial Flask application that displays your name when it is added to the URL.

# Setup
To Run this application, follow these steps:

1. Clone this repository to your development environment.
2. Change to the directory (e.g. `cd flasky`)
3. Create a virtual environment using `virtualenv venv`
4. Activate the virtual environmen using `source venv/bin/activate`
5. Run `pip install -r requirements.txt`
6. Once that is finished start the development server using `venv/bin/python app.py`
7. Next, browse to http://0.0.0.0:8080/ , you should see **Hello person** displayed.
8. Now try adding your name to the end of the URL, e.g. http://0.0.0.0:8080/John . You should then see **Hello John** displayed.
