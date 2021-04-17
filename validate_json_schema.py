#!/usr/bin/env python3
"""
validate
"""
import json
import argparse  # https://docs.python.org/3.3/library/argparse.html

# https://realpython.com/command-line-interfaces-python-argparse/
from jsonschema import validate

import json_schema


def validate_json(dict_to_validate: dict, schema_to_compare: dict) -> bool:
    """
    a function
    """
    validate(instance=dat, schema=json_schema.schema)
    return True


if __name__ == "__main__":

    theparser = argparse.ArgumentParser(
        description="validate JSON against schema", allow_abbrev=False
    )

    # required positional argument
    # it is possible to constrain the input to a range; see https://stackoverflow.com/a/25295717/1164295
    theparser.add_argument("JSONfilename", type=str, help="filename of JSON to parse")

    args = theparser.parse_args()

    with open(args.JSONfilename) as json_file:
        dat = json.load(json_file)

    validate_json(dat, json_schema.schema)

    print("Successfully validated file against schema")
