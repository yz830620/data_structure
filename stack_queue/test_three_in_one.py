import pytest
from three_in_one import ThreeInOne

@pytest.fixture
def three_in_one():
    return ThreeInOne()


class TestThreeInOne:
    """class for practicing test driven design"""
    def test_three_in_one(self, three_in_one):
        assert three_in_one is not None

    def test_stack_is_empty(self, three_in_one):
        assert three_in_one.stack_is_empty(stack_num=3) == True

    def test_stack_is_not_full(self, three_in_one):
        assert three_in_one.stack_is_full(stack_num=3) == False