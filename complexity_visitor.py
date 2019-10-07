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


        computing complexity of all the python files in
        the airflow folder for example:

            find airflow -name "*.py" | xargs -L 1 python complexity_visitor.py > airflow-analysis.csv

        sorting the outputs based on their complexity:

            cat airflow-analysis.csv | sort --field-separator=',' --key=3 -n

        should result in something like this:

            airflow/airflow/contrib/hooks/spark_jdbc_hook.py, _build_jdbc_application_arguments, 14
            airflow/airflow/gcp/hooks/bigquery.py, run_load, 16
            airflow/airflow/gcp/hooks/bigquery.py, run_query, 17
            airflow/airflow/gcp/operators/spanner.py, _validate_inputs, 18
            airflow/airflow/contrib/hooks/spark_submit_hook.py, _build_spark_submit_command, 25

        surely, you would get different results with a more intelligent
        implementation of the complexity

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

        # important to call, since this function
        # calls visit on every one of the children
        self.generic_visit(fundef)

        self.current_function = ""

    def visit_If(self, if_):
        if self.function_complexity.get(self.current_function):
            self.function_complexity[self.current_function] += 1
        else:
            self.function_complexity[self.current_function] = 1

        self.generic_visit(if_)


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
