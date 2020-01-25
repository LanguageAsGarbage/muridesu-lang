from muridesu.parse_stmts import parse_stmts
from importlib.util import source_hash, MAGIC_NUMBER
import marshal


def _w_long(x):
    return (int(x) & 0xFFFFFFFF).to_bytes(4, 'little')


def _code_to_hash_pyc(code, source_hash, checked=True):
    "Produce the data for a hash-based pyc."
    data = bytearray(MAGIC_NUMBER)
    flags = 0b1 | checked << 1
    data.extend(_w_long(flags))
    assert len(source_hash) == 8
    data.extend(source_hash)
    data.extend(marshal.dumps(code))
    return data


def comp(path: str, out: str, raw_bytecode: bool = False):
    with open(path, 'r') as f:
        source = f.read()
        mod = parse_stmts(source, path)
    code = compile(mod, path, mode='exec')

    with open(out, 'wb') as f:
        if raw_bytecode:
            f.write(marshal.dumps(code))
            return
        data = _code_to_hash_pyc(code, source_hash(source.encode('utf8')))
        f.write(data)

def main():
    from argser import call
    call(comp)