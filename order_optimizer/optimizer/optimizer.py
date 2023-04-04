import logging
from order_optimizer.common.constants import EXPECTED_ORDER_INPUTS_AND_TYPES
from order_optimizer.contract.order import Order

logger = logging.getLogger(__name__)


class OrderOptimizer:

    def __init__(self, config=None):
        if config:
            self.expected_inputs_and_types = config.get("expected_inputs_and_types")

        self.expected_inputs_and_types = EXPECTED_ORDER_INPUTS_AND_TYPES

    def optimize(self, order_list):
        order_list = self.to_order_object(order_list)
        order_list = self.get_possible_orders(order_list)
        return self.get_optimal_contracts(order_list)

    @staticmethod
    def to_order_object(order_list):
        return [Order(order) for order in order_list]

    @staticmethod
    def generate_next_orders(ref_order, order_list):
        return [order for order in order_list if order.start >= ref_order.end]

    def get_possible_orders(self, order_list):
        for i, order in enumerate(order_list):
            next_order_list = self.generate_next_orders(order, order_list[i:])
            order.set_next_orders(next_order_list)
        return order_list

    @staticmethod
    def get_optimal_contracts(order_list):
        possible_paths = []
        possible_profits = []

        # get all possible paths
        for order in order_list:
            possible_paths += order.tree2list()

        # calc possible profits
        for path in possible_paths:
            if isinstance(path, list):
                cum_profit = 0
                for o in path:
                    cum_profit += o.price
                possible_profits.append(cum_profit)
            else:
                possible_profits.append(o.price)

        paths_profits_list = list(zip(possible_paths, possible_profits))
        paths_profits_list.sort(key=lambda x: x[1], reverse=True)

        income = int(paths_profits_list[0][1])
        path_in_dict = [order.to_json() for order in paths_profits_list[0][0]]
        path_in_str = [order.get('name') for order in path_in_dict]

        result = {"income": income,
                  "path": path_in_str
                  }

        return result
