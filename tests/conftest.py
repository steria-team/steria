import pytest
# from steriaserver import app
# from steria.steriaserver import app


@pytest.fixture
def client():
    app.config['TESTING'] = True

    with app.test_client() as client:
        yield client
