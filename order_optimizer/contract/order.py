import json


class Order:
    def __init__(self, order):
        self.name = order.name
        self.start = order.start
        self.duration = order.duration
        self.price = order.price
        self._next_order = []

    @property
    def end(self):
        return self.start + self.duration

    def set_next_orders(self, sub_order_ls):
        self._next_order = sub_order_ls

    def tree2list(self):
        if len(self._next_order) == 0:
            return [self]
        else:
            node_list = [[self] + next_order.tree2list() for next_order in self._next_order]
            return node_list

    def __repr__(self):
        return {
            'name': self.name,
            'start': self.start,
            'duration': self.duration,
            'price': self.price
        }

    def to_json(self):
        return {
            'name': self.name,
            'start': self.start,
            'duration': self.duration,
            'price': self.price
        }
