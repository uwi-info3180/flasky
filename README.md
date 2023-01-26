# Flasky

A trivial Flask application that displays your name when it is added to the URL.

# Setup

To Run this application, ensure you have installed Python 3 and follow these steps:

1. Clone this repository to your development environment.
2. Change to the directory (e.g. `cd flasky`)
3. Create a virtual environment using `python -m venv venv`. In some cases you may need to use `python3 -m venv venv`.
4. Activate the virtual environment using `source venv/bin/activate` or on Windows use `.\venv\Scripts\activate`.
5. Run `pip install -r requirements.txt`
6. Once that is finished, start the built-in development server using `flask run`.
7. Next, open your web browser and go to **http://127.0.0.1:5000/** , you should see **This is my homepage** displayed.
8. Now try adding your **/hello/(yourname)** to the end of the URL, e.g. __http://127.0.0.1:5000/hello/Lauren__ . You should then see **Hello Lauren** displayed in the heading on the page.
9. Explore the code in this repository to learn more about how this was done.
