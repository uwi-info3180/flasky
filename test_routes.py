import pytest
from flask import Flask
from app import app as flask_app

@pytest.fixture()
def app():
    """fixtures allow writing pieces of code that are reusable across tests."""
    # app = Flask(__name__)
    # app.config.update({
    #     "TESTING": True,
    # })

    # other setup can go here

    yield flask_app

    # clean up / reset resources here


@pytest.fixture()
def client(app):
    return app.test_client()

@pytest.fixture()
def runner(app):
    return app.test_cli_runner()

def test_homepage(client):
    response = client.get("/")

    assert response.status_code == 200
    assert b"This is my homepage" in response.data

def test_hello(client):
    response = client.get("/hello/")

    assert response.status_code == 200
    assert b"Hello" in response.data

def test_hello_with_name(client):
    response = client.get("/hello/Yannick")

    assert response.status_code == 200
    assert b"Hello Yannick" in response.data

def test_about_page(client):
    response = client.get("/about")

    assert response.status_code == 200
    assert b"About Flask" in response.data