"""Utility functions."""

__author__ = "730439074"
from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []

    file_handle = open(filename, "r", encoding="utf8")

    csv_reader = DictReader(file_handle)

    for row in csv_reader:
        result.append(row)
        file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Product a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Tranform a row-oriented table to a column- oriented table."""
    result: dict[str, list[str]] = {}

    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)

    return result


def head(column: dict[str, list[str]], rows:int) -> dict[str, list[str]]:
    """Columnh based table with only the first N rows of data for each column."""
    result: dict[str, list[str]] = {}
    return result


def select(subject_race: dict[str,list[str]], subject_sex: list[str]) -> dict[str, list[str]]:
    """To produce a new column-based table."""
    result: dict[str, list[str]]
    return result


def concat(column_one: dict[str, list[str]], column_two: dict[str,list[str]]) -> dict[str, list[str]]:
    """New column based table with two culmn based tables combined."""

    new_column: dict[str, list[str]]

    for data in new_column:
        result[data]= column_one + column_two

        return result


def count(table: list[str])-> dict[str, int]
    """Preforming simple analysis with the data given."""
    result: dict[str, int] = []

    for data in table:
        item: int = data[counts]
        result.append(item)
    return results
