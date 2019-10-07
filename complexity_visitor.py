import ast
import sys


class ComplexityComputerVisitor(ast.NodeVisitor):
    """
        Evaluate the complexity of functions
        in a Python program

        Complexity of a function is defined in this
        program as being the "number of if conditionals
        in the program"

        Please think about how to refine it.

    """

    def __init__(self):
        self.function_complexity = dict()
        self.current_function = ""

    def compute_complexity(self, node):
        self.visit(node)
        return complexity_visitor.function_complexity.items()

    def _indent(self, code):
        return (" " * self.indent) + code

    def visit_FunctionDef(self, fundef):
        self.current_function = fundef.name

        for each in fundef.body:
            self.visit(each)

        self.current_function = ""

    def visit_If(self, if_):
        if self.function_complexity.get(self.current_function):
            self.function_complexity[self.current_function] += 1
        else:
            self.function_complexity[self.current_function] = 1


# take as input the file passed as argument
# alternatively use the fibonacci.py as input
if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = "fibonacci.py"

f = open(filename)
func_ast = ast.parse(f.read())

complexity_visitor = ComplexityComputerVisitor()
functions_and_complexities = complexity_visitor.compute_complexity(func_ast)

for fun, complexity in functions_and_complexities:
    print(filename + ", " + fun + ", " + str(complexity))
