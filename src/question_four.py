from logic import *

clauses = [expr("woman(jia)"), expr("man(john)"), expr("healthy(john)"), expr("wealthy(jia)"),
           expr("wealthy(x) & healthy(x) ==> traveler(x)")]
KB = FolKB(clauses)
traveler = fol_fc_ask(KB, expr("traveler(x)"))
healthy = fol_fc_ask(KB, expr("healthy(x)"))
wealthy = fol_fc_ask(KB, expr("wealthy(x)"))
print("\ntraveler?")
print(list(traveler))
print("\nhealthy?")
print(list(healthy))
print("\nwealthy?")
print(list(wealthy))
