from muridesu.wrap_parser import parse
from muridesu.helper import as_load
from ast import fix_missing_locations


def parse_stmts(source: str, filename=None):
    return fix_missing_locations(as_load(parse(source, filename)))
