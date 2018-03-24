import random
import math
import pyrosim
from robot import ROBOT
import numpy
import sys


class INDIVIDUAL:

    def __init__(self, i):

        self.ID = i

        self.genome = numpy.random.random((4,8)) * 2 - 1

        self.fitness = 0

    def Start_Evaluation(self, pb):

        self.sim = pyrosim.Simulator(eval_time=1800, play_blind=pb, play_paused=False)

        self.robot = ROBOT(self.sim, self.genome)

        # Start

        self.sim.start()

    def Compute_Fitness(self):

        self.sim.wait_to_finish()

        # distance into screen

        y = self.sim.get_sensor_data(sensor_id=self.robot.P4, svi=1)
        self.fitness = y[-1]

        del self.sim
        del self.robot

        #print(self.fitness)


    def Mutate(self):

        geneToMutateRow = random.randint(0, 3)
        geneToMutateCol = random.randint(0,7)

        self.genome[geneToMutateRow][geneToMutateCol] = random.gauss(self.genome[geneToMutateRow][geneToMutateCol],
                                                    math.fabs(self.genome[geneToMutateRow][geneToMutateCol]))

        if self.genome[geneToMutateRow][geneToMutateCol] > 1:
            self.genome[geneToMutateRow][geneToMutateCol] = 1

        if self.genome[geneToMutateRow][geneToMutateCol] < 1:
            self.genome[geneToMutateRow][geneToMutateCol] = -1


    def Print(self):

        print "[ ", self.ID, " ", self.fitness, "]",









