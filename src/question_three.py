from logic2 import *
x = Symbol("x")
y = Symbol("y")
x_hates_y = Symbol(f"hates({x}, {y})")
y_hates_x = Symbol(f"hates({y}, {x})")
enemies = Symbol(f"enemies({x}, {y})")
knowledge_one = And(Implication(And(x_hates_y, y_hates_x), enemies))
print(knowledge_one.formula())
# -------------------------------------------
p = Symbol(f"p({x})")
q = Symbol(f"q({x})")
r = Symbol(f"r({x})")
knowledge_two = And(Implication(p, Implication(q, r)))
print(knowledge_two.formula())