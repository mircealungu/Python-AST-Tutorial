import ast

p = ast.parse("def fun():"
              "    pass")
print(ast.dump(p))
