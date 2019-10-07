import ast
import inspect
from fibonacci import fibonacci


class JavascriptTranslator(ast.NodeVisitor):
    """

        Translate a python function into Javascript

    """

    def __init__(self):
        self.src = ""
        self.indent = 0

    def translate(self, node):
        self.visit(node)
        return self.src

    def _indent(self, code):
        return (" " * self.indent) + code


def convert_to_js(func):
    func_source = inspect.getsource(func)
    func_ast = ast.parse(func_source)

    translator = JavascriptTranslator()
    return translator.translate(func_ast)


print(convert_to_js(fibonacci))
