import ast
from astkit.render import SourceCodeRenderer

from copy import copy

# Program being generated
# =======================
# x = 2
# if (x == 4):
#     print(x)
# else:
#     x = (x + 1)
# print(x)

use_x = ast.Name(id="x", ctx=ast.Load())
assign_x = ast.Name(id="x", ctx=ast.Store())
one = ast.Num(n=1)
two = ast.Num(n=2)
four = ast.Num(n=4)

# x=2
initial_assign = ast.Assign(targets=[copy(assign_x)], value=copy(two))
initial_assign.lineno = 1
initial_assign.col_offset = 0
ast.fix_missing_locations(initial_assign)  # applies lineno and col_offset recursively to the subtree... not


# the if conditional
if_ = ast.If()
if_.test = ast.Compare()
if_.test.left = copy(use_x)
if_.test.ops = [ast.Eq()]
if_.test.comparators = [copy(four)]

# print(x)
print_x = ast.Expr(
    value=ast.Call(
        func=ast.Name(id="print", ctx=ast.Load()),
        args=[copy(use_x)],
        keywords=[]))

if_.body = [print_x]

x_plus_1 = ast.BinOp(left=copy(use_x),
                     op=ast.Add(),
                     right=copy(one))

assign_increment = ast.Assign(targets=[copy(assign_x)],
                              value=x_plus_1)

if_.orelse = [assign_increment]

if_.lineno = 2
if_.col_offset = 0
ast.fix_missing_locations(if_)


# print(x)
final_print = ast.Expr(
    value=ast.Call(
        func=ast.Name(id="print", ctx=ast.Load()),
        args=[copy(use_x)],
        keywords=[]))

final_print.lineno = 6
final_print.col_offset = 0
ast.fix_missing_locations(final_print)

# put everything together
mod = ast.Module(body=[
    initial_assign,
    if_,
    final_print])

code = compile(mod, '', 'exec')
print(type(code))

exec(code)
print(" ")

print(ast.dump(mod, include_attributes=True))
print(" ")

print(SourceCodeRenderer.render(mod))
