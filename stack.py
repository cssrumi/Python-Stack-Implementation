import copy


class Stack:
    def __init__(self):
        self.item = None

    def push(self, obj):
        if obj is None:
            raise ValueError("You can't push None object")
        if self.item is not None:
            self.item = Item(obj, self.item)
        else:
            self.item = Item(obj, None)

    def pop(self):
        item = self.item
        self.item = self.item.prev_item
        return item.obj

    def top(self):
        return self.item.obj

    def size(self):
        if self.item.obj is None:
            count = 0
        else:
            count = 1
        prev = self.item.prev_item
        while prev is not None:
            prev = prev.prev_item
            count += 1
        return count

    def empty(self):
        if self.item is None:
            return True
        return False

    def __add__(self, other):
        if other.__class__.__name__ == self.__class__.__name__:
            other = copy.deepcopy(other)
            if self.item is None:
                self.item = other.item
            else:
                other_item = other.item
                other_prev = other.item.prev_item
                while other_prev is not None:
                    other_item, other_prev = other_prev, other_prev.prev_item
                other_item.prev_item = self.item
            new_stack = Stack()
            new_stack.item = other.item
            return new_stack
        else:
            raise ValueError(
                '"You can only add Stack objects.\n' +
                'To add objects to stack use .push() method"')

    def to_list(self):
        result = []
        if self.item is not None:
            item = self.item
            prev = item.prev_item
            result.append(item.obj)
            while prev is not None:
                result.append(prev.obj)
                prev = prev.prev_item

        return result

    def __iter__(self):
        return self

    def __next__(self):
        if self.item is None:
            raise StopIteration
        result = self.pop()
        return result


class Item:
    def __init__(self, obj, prev_item):
        self.obj = obj
        self.prev_item = prev_item
