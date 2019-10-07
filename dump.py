import ast

"""
    To explore the ast for a given 
    construct first parse the AST from
    a string version of the code; then
    dump the AST object. 
"""

p = ast.parse("def fun():"
              "    pass")
print(ast.dump(p))
