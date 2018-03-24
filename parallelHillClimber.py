import random
import pyrosim
import matplotlib.pyplot as plt
from robot import ROBOT
import copy
import pickle
from individual import INDIVIDUAL
from population import POPULATION

parents = POPULATION(10)

parents.Evaluate(True)

parents.Print()

for g in range(1, 200):

    children = copy.deepcopy(parents)

    children.Mutate()

    children.Evaluate(True)

    parents.ReplaceWith(children)

    print g,

    parents.Print()

parents.Evaluate(False)



# parent = INDIVIDUAL()
# parent.evaluate(True)
#
# for i in range(0, 100):
#
#     child = copy.deepcopy(parent)
#     child.mutate()
#     child.evaluate(True)
#
#     print("[g: %s] [pw: %s] [p: %s] [c: %s]" % (i+1, parent.genome, parent.fitness, child.fitness))
#
#     if child.fitness > parent.fitness:
#
#         child.evaluate(True)
#         parent = child
#
#         # f = open("robot.p", "wb")
#         #
#         # pickle.dump(parent, f)
#         #
#         # f.close()
