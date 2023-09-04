""" Contains a class for testing the timings of polars """

import logging
import polars as pl

from polars_testing.utils import timer

logger = logging.getLogger(__name__)


class PolarsExample:
    """Class to test the timings of polars"""

    def __init__(self, input_path: str) -> None:
        self.input_data = self._read_csv(input_path)

    @timer
    @staticmethod
    def _read_csv(input_path: str) -> pl.DataFrame:
        """Read csv file into polars dataframe

        Args:
            input_path (str): Path to input csv files

        Returns:
            pl.DataFrame: polars DataFrame
        """
        logger.info("Reading data from %s", input_path)
        input_data: pl.DataFrame = pl.read_csv(input_path)
        return input_data

    @timer
    def filter_data(self, filter_column: str, filter_value: any) -> None:
        """Filter data

        Args:
            filter_column (str): Column to filter on
            filter_value (any): Value to filter on
        """
        logger.info("Filtering data on %s", filter_column)
        self.input_data = self.input_data.filter(pl.col(filter_column) < filter_value)

    @timer
    def aggregate_data(self, group_column: str, aggregate_function: str) -> pl.DataFrame:
        """Aggregate data with a column and function

        Args:
            group_column (str): Name of column to group by
            aggregate_function (str): Name of function for aggregation
        """
        logger.info(
            "Grouping data by %s and aggregating with %s",
            group_column,
            aggregate_function,
        )
        self.input_data = self.input_data.groupby(group_column).agg(pl.col("value").sum())

    @timer
    def write_data(self, output_path: str) -> None:
        """Write output data to path

        Args:
            output_path (str): Path to write output data
        """
        logger.info("Writing data to %s", output_path)
        self.input_data.write_csv(output_path)
