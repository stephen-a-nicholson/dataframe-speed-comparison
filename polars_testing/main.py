""" Application to test the timings of polars """

import argparse
import logging
from polars_testing.polars_example import PolarsExample

logging.basicConfig(filename="timings.log", level=logging.INFO)

parser = argparse.ArgumentParser()

parser.add_argument("input_path", help="path to input csv files", type=str)

args = parser.parse_args()


def main() -> None:
    """Test timings of polars"""
    res: PolarsExample = PolarsExample(input_path=args.input_path)
    res.filter_data(filter_column="test", filter_value=2000)


if __name__ == "__main__":
    main()
