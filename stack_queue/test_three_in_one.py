import pytest
from three_in_one import ThreeInOne
@pytest.fixture
def three_in_one():
    return ThreeInOne(3)


class TestThreeInOne:
    """class for practicing test driven design"""
    def test_three_in_one(self, three_in_one):
        assert three_in_one is not None

    def test_stack_is_empty(self, three_in_one):
        assert three_in_one.stack_is_empty(stack_num=2) == True

    def test_stack_is_not_full(self, three_in_one):
        assert three_in_one.stack_is_full(stack_num=2) == False

    def test_add_value_to_stack(self, three_in_one):
        stack_num = 0
        value = 5
        three_in_one.add_value_to_stack(stack_num=stack_num , value=value)
        assert three_in_one.stacks[stack_num][-1] == value 

    def test_after_add_not_empty(self, three_in_one):
        three_in_one.add_value_to_stack(stack_num=0 , value=5)
        assert three_in_one.stack_is_empty(stack_num=0) == False

    def test_full_after_adding_capacity_numbers(self, three_in_one):
        three_in_one.add_value_to_stack(stack_num=0 , value=5)
        three_in_one.add_value_to_stack(stack_num=0 , value=5)
        three_in_one.add_value_to_stack(stack_num=0 , value=5)
        assert three_in_one.stack_is_full(stack_num=0) == True

    def test_full_can_not_add_value(self, three_in_one):
        three_in_one.add_value_to_stack(stack_num=0 , value=5)
        three_in_one.add_value_to_stack(stack_num=0 , value=5)
        three_in_one.add_value_to_stack(stack_num=0 , value=5)
        assert three_in_one.add_value_to_stack(stack_num=0 , value=5) == False

    def test_pop_value_from_empty_stack(self, three_in_one):
        assert three_in_one.pop_value_from_stack(stack_num=0) == False
        
    def test_pop_value_from_stack(self, three_in_one):
        three_in_one.add_value_to_stack(stack_num=0 , value=5)
        assert three_in_one.pop_value_from_stack(stack_num=0) == 5

    def test_remove_all_stacks(self, three_in_one):
        three_in_one.add_value_to_stack(stack_num=0 , value=5)
        three_in_one.add_value_to_stack(stack_num=1 , value=5)
        three_in_one.add_value_to_stack(stack_num=2 , value=5)
        three_in_one.remove_all_stacks()
        assert three_in_one.stack_is_empty(stack_num=0) == True
        assert three_in_one.stack_is_empty(stack_num=1) == True
        assert three_in_one.stack_is_empty(stack_num=2) == True
