import json


def test_index(app, client):
    del app
    res = client.get('/')
    assert res.status_code == 400

def test_index1(app, client):
    del app
    res = client.get('/')
    assert res.status_code == 200

def test_index2(app, client):
    del app
    res = client.get('/')
    assert res.status_code == 200
