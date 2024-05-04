"""
Dataframe Speed Comparison

This module compares the performance of DuckDB, Polars, and Pandas using a large and complex dataset.
"""

import time
from typing import Tuple, List
import duckdb
import pandas as pd
import polars as pl
import numpy as np
import matplotlib.pyplot as plt

# Resource management for DuckDB
duckdb_config = {
    "memory_limit": "4GB",  # Setting a memory limit of 4GB
    "threads": 4,  # Limit DuckDB to use up to 4 threads
}


def configure_duckdb():
    con = duckdb.connect(config=duckdb_config)
    return con


def complex_operations(
    df: pd.DataFrame, pdf: pl.DataFrame
) -> Tuple[float, float, float]:
    """
    Perform complex operations (filter, join, aggregation) on the provided DataFrames.

    Args:
        df (pd.DataFrame): Pandas DataFrame.
        pdf (pl.DataFrame): Polars DataFrame.

    Returns:
        Tuple[float, float, float]: Time taken by DuckDB, Polars, and Pandas to perform the operations.
    """
    con = configure_duckdb()
    con.register("df", df)

    # DuckDB Operations
    start_time = time.time()
    _ = con.execute(
        "SELECT C, COUNT(*) FROM df GROUP BY C"
    ).fetchall()
    duckdb_time = time.time() - start_time

    # Polars Operations
    start_time = time.time()
    _ = pdf.groupby("C").agg(pl.count())
    polars_time = time.time() - start_time

    # Pandas Operations
    start_time = time.time()
    _ = df.groupby("C").size()
    pandas_time = time.time() - start_time

    return duckdb_time, polars_time, pandas_time


def generate_graph(labels: List[str], times: List[float]) -> None:
    """
    Generate a bar chart comparing the time taken by different libraries.

    Args:
        labels (List[str]): Labels for the libraries.
        times (List[float]): Times taken by the libraries.

    Returns:
        None
    """
    plt.figure(figsize=(8, 6))
    bars = plt.bar(labels, times, color=["#4F81BD", "#C0504D", "#9BBB59"])
    plt.xlabel("Library", fontsize=12, labelpad=15)
    plt.ylabel("Time (seconds)", fontsize=12, labelpad=15)
    plt.title(
        "Performance Comparison of DuckDB, Polars, and Pandas",
        fontsize=14,
        pad=20,
    )
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    plt.grid(axis="y", linestyle="--", alpha=0.7)

    # Adding data labels on top of each bar
    for bar in bars:
        yval = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            yval,
            round(yval, 4),
            ha="center",
            va="bottom",
            fontsize=10,
            color="black",
        )

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    # Generate a larger and more complex dataset
    num_rows = 10**7
    data = {
        "A": np.random.randint(0, 100, size=num_rows),
        "B": np.random.rand(num_rows),
        "C": np.random.choice(["X", "Y", "Z"], num_rows),
        "D": np.random.normal(0, 1, num_rows),
    }
    df = pd.DataFrame(data)
    pdf = pl.DataFrame(data)

    # Measure the time taken by each library for complex operations
    duckdb_time, polars_time, pandas_time = complex_operations(df, pdf)

    # Generate graphs
    labels = ["DuckDB", "Polars", "Pandas"]
    times = [duckdb_time, polars_time, pandas_time]
    generate_graph(labels, times)
