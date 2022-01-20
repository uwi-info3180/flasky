# Flasky

A trivial Flask application that displays your name when it is added to the URL.

# Setup

To Run this application, ensure you have installed Python 3 and follow these steps:

1. Clone this repository to your development environment.
2. Change to the directory (e.g. `cd flasky`)
3. Create a virtual environment using `python -m venv venv`. In some cases you may need to use `python3 -m venv venv`.
4. Activate the virtual environment using `source venv/bin/activate` or on Windows use `.\venv\Scripts\activate`.
5. Run `pip install -r requirements.txt`
6. Once that is finished start the development server using `python app.py` (in some cases `python3 app.py`.
7. Next, browse to http://localhost:8080/ , you should see **Hello person** displayed.
8. Now try adding your name to the end of the URL, e.g. http://localhost:8080/John . You should then see **Hello John** displayed.
