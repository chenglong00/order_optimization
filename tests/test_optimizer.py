import unittest

from order_optimizer.optimizer.optimizer import OrderOptimizer
from order_optimizer.common.utils import dict_to_contract
import pydantic


class OrderOptimizerTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self._order_optimizer = OrderOptimizer()
        self._order_ls = [
            {"name": "Contract1", "start": 0, "duration": 5, "price": 10},
            {"name": "Contract2", "start": 3, "duration": 7, "price": 14},
            {"name": "Contract3", "start": 5, "duration": 9, "price": 8},
            {"name": "Contract4", "start": 5, "duration": 9, "price": 7}
        ]

        self._wrong_order_ls = [
            {"nam": "Contract1", "star": 0, "duratio": 5, "pric": 10},  # wrong input
            {"name": 123, "start": "a", "duration": "b", "price": "c"},  # wrong type
            {"name": "Contract1" * 100, "start": 0, "duration": 5, "price": 10}  # wrong len
        ]

    def test_optimize(self):
        order_list = dict_to_contract(self._order_ls)
        result = self._order_optimizer.optimize(order_list)

        self.assertIsInstance(result.get('income'), int)
        self.assertIsInstance(result.get('path'), list)
        for p in result.get('path'):
            self.assertIsInstance(p, str)

        print(result)
        print(type(result.get('income')))
        print(type(result.get('path')[0]))

    def test_optimize_error(self):
        with self.assertRaises(pydantic.error_wrappers.ValidationError) as context:
            self._order_optimizer.optimize(dict_to_contract(self._wrong_order_ls[0:1]))

        # print(context.exception)
        self.assertTrue("none is not an allowed value" in str(context.exception))

        with self.assertRaises(pydantic.error_wrappers.ValidationError) as context:
            self._order_optimizer.optimize(dict_to_contract(self._wrong_order_ls[1:2]))

        # print(context.exception)
        self.assertTrue("value is not a valid integer" in str(context.exception))

        with self.assertRaises(pydantic.error_wrappers.ValidationError) as context:
            self._order_optimizer.optimize(dict_to_contract(self._wrong_order_ls[2:3]))

        # print(context.exception)
        self.assertTrue("ensure this value has at most 64 characters" in str(context.exception))
