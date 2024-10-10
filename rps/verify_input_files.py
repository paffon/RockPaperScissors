"""
This module provides utility functions for validating configuration files, specifically for
ensuring that short names and relationship mappings are correctly formatted and contain no
duplicates or invalid entries.

These functions are primarily used to check configuration files for a game or system where
short names and relationships between items are crucial.
"""

from pandas import DataFrame
from typing import List, Tuple


def assert_no_duplicates(elements: List[str], message: str):
    """
    Asserts that there are no duplicate elements in the provided list.

    :param elements: List of elements to check for duplicates.
    :param message: Error message to display if duplicates are found.

    :raises AssertionError: If duplicates are found in the list.
    """
    if len(elements) != len(set(elements)):
        duplicates = {x for x in elements if elements.count(x) > 1}
        raise AssertionError(f"{message} {duplicates}")


def assert_all_included(elements: List[str], pool: List[str], message: str):
    """
    Asserts that all elements in the provided list exist within the pool.

    :param elements: List of elements to check for inclusion in the pool.
    :param pool: List representing the valid pool of elements.
    :param message: Error message to display if elements are missing from the pool.

    :raises AssertionError: If any element in the list is not found in the pool.
    """
    if not all([x in pool for x in elements]):
        missing = {x for x in elements if x not in pool}
        raise AssertionError(f"{message} {missing}. Allowed: {pool}")


def validate_short_names(short_names: List[Tuple[str, str]]):
    """
    Validates that there are no duplicates in short names and that no short names
    are used as full names in the dataset.

    :param short_names: List of tuples, where each tuple contains a short name and a full name.

    :raises AssertionError: If duplicates are found in short names or if any short names
                            are also used as full names.
    """
    # verify no duplicates in short_names
    for idx, shorts_or_names in [(0, 'shorts'), (1, 'names')]:
        objects: List[str] = [tup[idx] for tup in short_names]
        assert_no_duplicates(elements=objects,
                             message=f'short_names.json: duplicates found in {shorts_or_names}')
    shorts_and_names: List[str] = [tup[0] for tup in short_names] + [tup[1] for tup in short_names]
    assert_no_duplicates(elements=shorts_and_names,
                         message=f'short_names.json: some short names appear as full names')


def validate_relationship(short_names: List[str], relationship: DataFrame):
    """
    Validates that the relationship DataFrame has no duplicate indices or columns,
    all indices and columns are known short names, and that the DataFrame represents
    a 1-to-1 relationship. Also checks that all values in the DataFrame are 0, 1, or 2.

    :param short_names: List of known short names to check the relationship index and columns against.
    :param relationship: DataFrame containing relationship mappings with indices and columns.

    :raises AssertionError: If any validation checks fail, such as duplicates or invalid values.
    """
    relationship_index = relationship.index.to_list()
    relationship_columns = relationship.columns.to_list()

    # Verify no duplications in index or columns
    assert_no_duplicates(elements=relationship_index,
                         message='relationship.csv: index contains duplicates')
    assert_no_duplicates(elements=relationship_columns,
                         message='relationship.csv: columns contain duplicates')

    # Verify that the relationship map only contains known short names
    assert_all_included(elements=relationship_index, pool=short_names,
                        message='relationship.csv: index contains unknown values')
    assert_all_included(elements=relationship_columns, pool=short_names,
                        message='relationship.csv: columns contain unknown values')

    # Verify that the relationship map is a 1-to-1 relationship
    assert_all_included(elements=relationship_index, pool=relationship_columns,
                        message='relationship.csv: index contains elements not present in columns')
    assert_all_included(elements=relationship_columns, pool=relationship_index,
                        message='relationship.csv: columns contain elements not present in index')

    # Verify that the relationship map only contains 0, 1, or 2 int values
    all_values: List[int] = relationship.values.flatten().tolist()
    allowed_values: List[int] = [0, 1, 2]
    values_are_allowed: List[bool] = [x in allowed_values for x in all_values]
    if not all(values_are_allowed):
        bad_values: List[int] = [x for x in all_values if x not in allowed_values]
        raise AssertionError(f'relationship.csv: found bad values {bad_values}.'
                             f' Allowed values: {allowed_values}')


def validate_config_files_input(short_names: List[Tuple[str, str]], relationship: DataFrame):
    """
    Validates the input consisting of short names and a relationship DataFrame.
    Performs validations on short names and the relationship map.

    :param short_names: List of tuples, where each tuple contains a short name and a full name.
    :param relationship: DataFrame containing relationship mappings with indices and columns.

    :raises AssertionError: If any validation checks fail in short names or relationship mappings.
    """
    validate_short_names(short_names)
    shorts = [tup[0] for tup in short_names]
    validate_relationship(shorts, relationship)
