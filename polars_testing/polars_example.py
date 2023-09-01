""" Contains functions for testing the timings of polars """

import logging
import polars as pl

from polars_testing.utils import timer

logger = logging.getLogger(__name__)


@timer
def polars_transformations(input_path: str) -> pl.DataFrame:
    """Test timings of polars transformations

    Args:
        input_path (str): Path to input csv files

    Returns:
        pl.DataFrame: polars DataFrame
    """
    logger.info("Reading data from %s", input_path)
    input_data: pl.DataFrame = pl.read_csv(input_path)
    return input_data
