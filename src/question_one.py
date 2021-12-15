from logic2 import *

carrots = Symbol("carrots")
orange = Symbol("orange")
knowledge_one = And(Implication(carrots, orange))
print(knowledge_one.formula())

# ----------------------------------------------
person = Symbol("person")
vegetarian = Symbol(f"vegetarian({person})")
likes = Symbol("likes")
person_likes_carrots = Symbol(f"like({person}, {carrots})")
knowledge_two = And(Implication(person_likes_carrots, vegetarian))
print(knowledge_two.formula())
# ----------------------------------------------
student = Symbol("student")
study_hard = Symbol(f"study_hard({student})")
pass_exam = Symbol(f"pass_exam({student})")
knowledge_three = And(Implication(study_hard, pass_exam))
print(knowledge_three.formula())

# ----------------------------------------------
Pass = Symbol("? pass")
knowledge_four = And(Pass)
print(knowledge_four.formula())
# ----------------------------------------------
professor = Symbol("professor")
course = Symbol ("course")
teaches = Symbol(f"teaches({professor},{course})")
knowledge_five = And(teaches)
print(knowledge_five.formula())
# ----------------------------------------------
x = Symbol("x")
y = Symbol("y")
hates = Symbol(f"hates({x},{y})")
fights = Symbol(f"fights({x},{y})")
enemies = Symbol(f"enemies({x},{y})")
knowledge_six = And(Implication(And(hates, fights), enemies))
print(knowledge_six.formula())