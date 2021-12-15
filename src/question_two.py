from logic2 import *

maria = Symbol("maria")
author = Symbol("peter lucas")
reads = Symbol(f" read ({maria}, logic programming book)")
by = Symbol(f"by {author}")
knowledge_one = And(reads, by)
print(knowledge_one.formula())
# -------------------------------------------
x = Symbol("x")
is_girl = Symbol(f"is_girl({x})")
shopping = Symbol("shopping")
likes = Symbol(f"likes({x}, {shopping})")
knowledge_two = And(Implication(likes, is_girl))
print(knowledge_two.formula())
# -------------------------------------------
who = Symbol("?")
knowledge_three = And(who, likes)
print(knowledge_three.formula())
# -------------------------------------------
city = Symbol("city")
kirke = Symbol("kirke")
is_big = Symbol(f"is_big({city})")
is_crowdy = Symbol(f"is_crowdy({city})")
hates = Symbol(f"hates({kirke},{city})")
knowledge_four = And(Implication(And(is_big, is_crowdy), hates))
print(knowledge_four.formula())
# -------------------------------------------