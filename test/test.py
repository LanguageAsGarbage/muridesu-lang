from muridesu.wrap_parser import parse
from muridesu.helper import as_load
from ast import fix_missing_locations
from astpretty import pprint
pprint(fix_missing_locations(as_load(parse("""
func f(x){
    a = 2;
    b = 3;
    (c, d) = (a, b);
    return x
}
"""))))