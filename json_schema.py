#!/usr/bin/env python3
"""
for a tutorial on how to create a schmea, see
https://json-schema.org/understanding-json-schema/about.html#about
https://json-schema.org/understanding-json-schema/reference/object.html#pattern-properties
"""

schema = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {"/": {}},
    "patternProperties": {
        "^([0-9]+)$": {
            "type": "array",
            # https://json-schema.org/understanding-json-schema/reference/array.html
            # https://json-schema.org/understanding-json-schema/reference/numeric.html
            "items": {"type": "integer"},
        }
    },
    "additionalProperties": False,
}
