import pytest

import crud 

@pytest.fixture()
def client():

    crud.users.clear()
    crud.current_id = 1 
    crud.app.testing = True

    with crud.app.test_client() as test_client:
        yield test_client
