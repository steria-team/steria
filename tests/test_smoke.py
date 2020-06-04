from flask import wrappers

def test_smoke_test(client):
    res: wrappers.Response = client.get('/test')
    assert res.data.decode('utf-8') == 'test'