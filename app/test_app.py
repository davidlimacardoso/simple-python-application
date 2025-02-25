# tests/test_app.py

import os
import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_hello_with_name(client):
    # Testa a rota principal com um nome
    response = client.get('/David')
    assert response.status_code == 200
    assert b'Hello David!' in response.data  # Verifique se o nome está na resposta
    assert b'This application is an example' in response.data

def test_hello_without_name(client):
    # Testa a rota principal sem um nome
    response = client.get('/')
    assert response.status_code == 200
    assert b'Welcome!' in response.data  # Verifique se a mensagem de boas-vindas está na resposta
    assert b'This application is an example' in response.data

def test_healthcheck(client):
    # Testa a rota de healthcheck
    response = client.get('/healthcheck')
    assert response.status_code == 200
    assert b'Container is' in response.data  # Verifique se a mensagem de healthcheck está na resposta

def test_api(client):
    # Testa a rota da API sem ação
    response = client.get('/api')
    assert response.status_code == 200
    assert b'You are access:' in response.data  # Verifique se a frase está na resposta

    # Testa a rota da API com ação
    response = client.get('/api/v4/some_action')
    assert response.status_code == 200
    assert b'You are access:' in response.data  # Verifique se a frase está na resposta
    assert b'some_action' in response.data  # Verifique se a ação está na resposta