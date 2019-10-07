import ast
from copy import copy

# Program being generated
# =======================
# x = 2
# if (x == 4):
#     print(x)
# else:
#     x = (x + 1)
# print(x)

# reusable variables
use_x = ast.Name(id="x",
                 ctx=ast.Load())
x_lhs = ast.Name(id="x",
                 ctx=ast.Store())
one = ast.Num(n=1)
two = ast.Num(n=2)
four = ast.Num(n=4)

# initial assign
initial_assign = ast.Assign(
    targets=[copy(x_lhs)],
    value=copy(two))

initial_assign.lineno = 1
initial_assign.col_offset = 0
ast.fix_missing_locations(initial_assign)

# print statement
print_statement = ast.Expr(
    value=ast.Call(
        func=ast.Name(id="print", ctx=ast.Load()),
        args=[use_x],
        keywords=[]
    )
)
print_statement.lineno = 2
print_statement.col_offset = 0
ast.fix_missing_locations(print_statement)



if_ = ast.If()
if_.test = ast.Compare()
if_.test.left = copy(use_x)
if_.test.ops = [ast.Eq()]
if_.test.comparators = [copy(four)]

if_.body = [print_statement]

x_plus_1 = ast.BinOp(left=copy(use_x),
                     op=ast.Add(),
                     right=copy(one))

assign_increment = ast.Assign(targets=[copy(x_lhs)],
                              value=x_plus_1)

if_.orelse = [assign_increment]

if_.lineno = 2
if_.col_offset = 0
ast.fix_missing_locations(if_)

program = ast.Module(
    body=[
        initial_assign,
        if_,
        print_statement
    ]
)

code = compile(program, '', 'exec')
exec(code)

print(ast.dump(if_))
