class OptimizerException(Exception):
    """
    Optimizer base exception. Handled at the outermost level.
    All other exception types are subclasses of this exception type.
    """


class DataException(OptimizerException):
    """
    Errors with input validation.
    Usually caused by errors in the input data.
    """


class OperationalException(OptimizerException):
    """
    Requires manual intervention and will stop the service..
    """
