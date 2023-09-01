""" Application to test the timings of polars """

import argparse
import logging
import polars as pl
from polars_testing.polars_example import polars_transformations

logging.basicConfig(filename="timings.log", level=logging.INFO)

parser = argparse.ArgumentParser()

parser.add_argument("input_path", help="path to input csv files", type=str)

args = parser.parse_args()


def main() -> None:
    """Test timings of polars"""
    res: pl.DataFrame = polars_transformations(input_path=args.input_path)
    print(res.head())


if __name__ == "__main__":
    main()
