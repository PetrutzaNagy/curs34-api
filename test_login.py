import json

import requests as requests


def test_login_negative():
    response = requests.post('https://thinking-tester-contact-list.herokuapp.com/users/login')
    assert response.status_code == 401

#data - e body-ul care il trimitem in postman - ce date trimitem noi la server
def test_login():
    # pt ca sa putem trimite un dictionar sub forma de json convertim un dictionar
    credentials = {
        "email": "curs34@test.com", "password": "test1234"
    }
    response = requests.post('https://thinking-tester-contact-list.herokuapp.com/users/login', json = credentials)
    print(response.text)
    assert response.status_code == 200
    response_body = response.json()
    assert response_body["user"]["firstName"] == "test"
    assert response_body["user"]["email"] == "curs34@test.com"


def test_login_negative2():
    # pt ca sa putem trimite un dictionar sub forma de json convertim un dictionar
    credentials = {
        "email": "curs34@test.com", "password": "test123"
    }
    response = requests.post('https://thinking-tester-contact-list.herokuapp.com/users/login', json = credentials)
    print(response.text)
    assert response.status_code == 401
