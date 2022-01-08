


class ThreeInOne:
    def __init__(self, stack_qty):
        self.stack_qty = stack_qty
        self.stacks = [[]] * stack_qty

    def stack_is_empty(self, stack_num):
        if self.stacks[stack_num]:
            return False
        else:
            return True

    def stack_is_full(self, stack_num):
        return False

    def add_value_to_stack(self, stack_num, value):
        self.stacks[stack_num].append(value)