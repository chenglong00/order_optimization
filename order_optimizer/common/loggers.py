import logging
from order_optimizer.common.constants import LOGFORMAT, DATEFORMAT

logger = logging.getLogger(__name__)


def setup_simple_logging():
    # set up simple logging
    logging.basicConfig(
        level=logging.DEBUG,
        format=LOGFORMAT,
        datefmt=DATEFORMAT
    )
