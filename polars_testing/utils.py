""" Contains utility functions for the application """

import logging
import functools
import time

logger = logging.getLogger(__name__)


def timer(func):
    """Decorator for functions

    Args:
        func (Any): Function to decorate

    Returns:
        Any: Decorated function
    """

    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        tic = time.perf_counter()
        value = func(*args, **kwargs)
        toc = time.perf_counter()
        elapsed_time = toc - tic
        logger.info("Elapsed time: %s seconds", f"{elapsed_time:0.4f}")
        return value

    return wrapper_timer
