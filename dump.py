import ast

p = ast.parse("print(x)")
print(ast.dump(p))
