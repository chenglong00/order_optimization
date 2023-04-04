from fastapi import FastAPI
from order_optimizer.optimizer.optimizer import OrderOptimizer
from order_optimizer.common.loggers import setup_simple_logging
import logging
from typing import List, Union
from order_optimizer.api.model import Contact, OptimizedResult, ErrorResult

app = FastAPI()
optimizer: OrderOptimizer = OrderOptimizer()
setup_simple_logging()

logger = logging.getLogger(__name__)


@app.post("/test")
def test():
    """ test server """
    logger.info("test endpoint called")
    return {"hello": "world"}


@app.post("/spaceship/optimize")  #
def optimize(order_list: List[Contact], response_model=Union[OptimizedResult, ErrorResult]):
    """ Optimize Orders """
    # = Body(None, desccription="Comma-separated list of orders")
    logger.info("optimize endpoint called")
    print(order_list)
    # try:
    result = optimizer.optimize(order_list)
        # result
    # except DataException as data_err:
    #     result = {"error_message": data_err,
    #               "error_code": 400}
    # except Exception as critical_err:
    #     result = {"error_message": critical_err,
    #               "error_code": 400}
    return result
