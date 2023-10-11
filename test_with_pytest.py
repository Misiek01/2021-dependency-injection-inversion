import pytest

@pytest.fixture
def output_fixture():
    return 4

def test_multiplication_of_two_times_two_equals_four(output_fixture):
    assert 2*2==output_fixture