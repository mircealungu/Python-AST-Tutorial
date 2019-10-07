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

    def visit_FunctionDef(self, defn):
        arglist = ",".join(name.arg
                           for name in
                           defn.args.args)
        js_defn = f"var {defn.name} = function ({arglist})"
        js_defn += "\n{\n"

        self.src += self._indent(js_defn)

        self.indent += 4
        for stmt in defn.body:
            self.visit(stmt)
        self.indent -= 4

        self.src += self._indent("}\n")

    def visit_If(self, if_):
        self.src += self._indent("if (")
        self.visit(if_.test)
        self.src += ") {\n"

        self.indent += 4
        for stmt in if_.body:
            self.visit(stmt)
        self.indent -= 4

        self.src += self._indent("}\n")

    def visit_Compare(self, compare):
        self.visit(compare.left)
        self.src += " "
        self.visit(compare.ops[0])
        self.src += " "
        self.visit(compare.comparators[0])

    def visit_Name(self, name):
        self.src += name.id

    def visit_Eq(self, eq):
        self.src += " == "

    def visit_Num(self, num):
        self.src += str(num.n)

    def visit_Add(self, add):
        self.src += "+"

    def visit_Call(self, call):
        self.visit(call.func)

    def visit_BinOp(self, binop):
        self.visit(binop.left)
        self.visit(binop.op)
        self.visit(binop.right)

    def visit_Return(self, retu):
        self.src += self._indent("return ")
        if retu.value:
            self.src += " "
            self.visit(retu.value)
        self.src += ";\n"

    def _indent(self, code):
        return (" " * self.indent) + code


def js(func):
    func_source = inspect.getsource(func)
    func_ast = ast.parse(func_source)

    translator = JavascriptTranslator()
    return translator.translate(func_ast)


print(js(fibonacci))
