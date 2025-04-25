import pytest

@pytest.fixture
def sample_data():
    return {"name": "Carey", "age": 30}

def test_user(sample_data):
    assert sample_data["name"] == "Carey"