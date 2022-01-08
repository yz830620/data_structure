class ThreeInOne:
    def __init__(self, stack_qty, capacity=3):
        self.stack_qty = stack_qty
        self.capacity = capacity
        self.stack = [0] * capacity
        self.stacks = [[]] * capacity

    def stack_is_empty(self, stack_num):
        if self.stacks[stack_num]:
            return False
        else:
            return True

    def stack_is_full(self, stack_num):
        if len(self.stacks[stack_num]) == self.capacity:
            return True
        else:
            return False

    def add_value_to_stack(self, stack_num, value):
        if not self.stack_is_full(stack_num):
            self.stacks[stack_num].append(value)
            return True
        else:
            print('Stack is full, not process')
            return False
