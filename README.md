# Dataframe Speed Comparison

This repository contains a Python module that compares the performance of three popular data manipulation libraries: DuckDB, Polars, and Pandas. The module generates a large dataset and performs a simple filtering operation on the data using each library. The time taken by each library to complete the operation is measured and displayed in a bar chart.

## Installation

You can install the project using [Poetry](https://python-poetry.org/):

```bash
git clone https://github.com/stephen-a-nicholson/dataframe-speed-comparison.git
cd dataframe-speed-comparison
poetry install
```

## Usage

To run the performance comparison, execute the following command:

```bash
poetry run python main.py
```

This will generate a large dataset, perform the filtering operation on the data using DuckDB, Polars, and Pandas, and display a bar chart comparing the time taken by each library.

## Dependencies

The project depends on the following Python libraries:

- DuckDB
- Pandas
- Polars
- NumPy
- Matplotlib

These dependencies are automatically installed when you run `poetry install`.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).