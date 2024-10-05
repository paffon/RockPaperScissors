import pandas as pd
from typing import List
import json

def assert_no_duplicates(elements: List[str], message: str):
    if len(elements) != len(set(elements)):
        duplicates = {x for x in elements if elements.count(x) > 1}
        raise AssertionError(f"{message} {duplicates}")

def assert_all_included(elements: List[str], pool: List[str], message: str):
    if not all([x in pool for x in elements]):
        missing = {x for x in elements if x not in pool}
        raise AssertionError(f"{message} {missing}")

relationship = pd.read_csv('../../data/relationship.csv', index_col=0)
# read json
with open('../../data/short_names.json', 'r') as f:
    short_names = json.load(f)

# verify no duplicates in short_names
for idx, shorts_or_names in [(0, 'shorts'), (1, 'names')]:
    objects: List[str] = [tup[idx] for tup in short_names]
    assert_no_duplicates(objects, f'short_names.json: duplicates found in {shorts_or_names}')

# Since a 1-to-1 relationship is asserted, the dictionaries will have the same length
shorts_to_names = {tup[0]: tup[1] for tup in short_names}
names_to_shorts = {tup[1]: tup[0] for tup in short_names}

# Relationship verifications
relationship_index = relationship.index.to_list()
relationship_columns = relationship.columns.to_list()

# Verify no duplications in index or columns
assert_no_duplicates(elements=relationship_index,
                     message='relationship.csv: index contains duplicates')
assert_no_duplicates(elements=relationship_columns,
                     message='relationship.csv: columns contain duplicates')

# Verify that the beats_map only contains known short names
assert_all_included(elements=relationship_index,
                    pool=list(shorts_to_names.keys()),
                    message='relationship.csv: index contains unknown short names')
assert_all_included(elements=relationship_columns,
                    pool=list(shorts_to_names.keys()),
                    message='relationship.csv: columns contain unknown short names')

# Verify that the beats_map is a 1-to-1 relationship
assert_all_included(elements=relationship_index,
                    pool=relationship_columns,
                    message='relationship.csv: index contains elements not present in columns')
assert_all_included(elements=relationship_columns,
                    pool=relationship_index,
                    message='relationship.csv: columns contain elements not present in index')

# verify that beats map only contains 0, 1 or 2 int values
all_values: List[int] = relationship.values.flatten().tolist()
allowed_values: List[int] = [0, 1, 2]
values_are_allowed: List[bool] = [x in allowed_values
                                  for x in all_values]

if not all(values_are_allowed):
    bad_values: List[int] = [x for x in all_values if x not in allowed_values]
    raise AssertionError(f'relationship.csv: found bad values {bad_values}.'
                         f' Allowed values: {allowed_values}')

pass