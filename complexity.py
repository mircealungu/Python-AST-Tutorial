import ast
import sys


class JavascriptTranslator(ast.NodeVisitor):
    """
        Translate a python function into Javascript
    """

    def __init__(self):
        self.src = ""
        self.indent = 0
        self.function_complexity = dict()
        self.current_function = ""

    def translate(self, node):
        self.visit(node)
        return self.src

    def _indent(self, code):
        return (" " * self.indent) + code

    def visit_FunctionDef(self, fundef):
        self.current_function = fundef.name

        arg_list = ",".join(name.arg for name in fundef.args.args)
        js_definition = f"var {fundef.name} = function ({arg_list})"
        js_definition += "{\n"
        self.src += js_definition

        for each in fundef.body:
            self.visit(each)

        self.src += "}\n"
        self.current_function = ""

    def visit_If(self, if_):
        if self.function_complexity.get(self.current_function):
            self.function_complexity[self.current_function] += 1
        else:
            self.function_complexity[self.current_function] = 1


f = open(sys.argv[1])
func_ast = ast.parse(f.read())

translator = JavascriptTranslator()
translated = translator.translate(func_ast)
print (translator.function_complexity)



