import ast
from rbnf_rts.routine import DQString

METACLASS = 'metaclass'

join_string_by_dot = '.'.join


class ExprContextFixer(ast.NodeVisitor):
    def __init__(self, ctx):
        self.ctx = ctx

    def _store_simply(self, node):
        if not hasattr(node, 'ctx') or not node.ctx:
            node.ctx = self.ctx

    def _store_recursively(self, node):
        if not hasattr(node, 'ctx') or not node.ctx:
            node.ctx = self.ctx
        self.generic_visit(node)

    visit_Name = _store_simply
    visit_Subscript = _store_recursively
    visit_Attribute = _store_recursively
    visit_Tuple = _store_recursively
    visit_List = _store_recursively
    visit_Starred = _store_recursively


_as_store = ExprContextFixer(ast.Store()).visit


def as_store(it):
    if hasattr(it, '_fields'):
        _as_store(it)
        return it
    return it


_as_load = ExprContextFixer(ast.Load()).visit


def as_load(it):
    if hasattr(it, '_fields'):
        _as_load(it)
        return it
    return it


def tuple_if_more_than_1(xs):
    if len(xs) is 1:
        return xs[0]
    return ast.Tuple(xs)


def mk_tuple(xs, is_tuple):
    is_tuple = len(xs) > 1 or is_tuple
    if is_tuple:
        return ast.Tuple(xs)
    return xs[0]


def loc(loc, n):
    if hasattr(n, '_fields'):
        n.lineno = loc[0] + 1
        n.col_offset = loc[1]
    return n


list_ = list
