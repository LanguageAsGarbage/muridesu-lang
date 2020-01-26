from muridesu.wrap_parser import parse
from muridesu.helper import as_load, lift
from ast import fix_missing_locations


def parse_stmts(source: str, filename=None):
    return fix_missing_locations(as_load(lift(parse(source, filename))))
