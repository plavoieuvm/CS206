import random
import pyrosim
import matplotlib.pyplot as plt
from robot import ROBOT
import copy
import pickle
from individual import INDIVIDUAL

parent = INDIVIDUAL()
parent.evaluate(True)

for i in range(0, 100):

    child = copy.deepcopy(parent)
    child.mutate()
    child.evaluate(True)

    print("[g: %s] [pw: %s] [p: %s] [c: %s]" % (i+1, parent.genome, parent.fitness, child.fitness))

    if child.fitness > parent.fitness:

        child.evaluate(True)
        parent = child

        # f = open("robot.p", "wb")
        #
        # pickle.dump(parent, f)
        #
        # f.close()

    # sim = pyrosim.Simulator(eval_time=500, play_paused=False)
    #
    # robot = ROBOT(sim, random.random()*2-1)
    #
    # # Start
    #
    # sim.start()
    #
    # sim.wait_to_finish()
    #
    # # y
    # sensorData = sim.get_sensor_data(sensor_id=robot.P4, svi=1)
    #
    # print(sensorData[-1])
    #
    # # Analyze sensor data
    #
    # f = plt.figure()
    #
    # panel = f.add_subplot(111)
    #
    # plt.plot(sensorData)
    #
    # panel.set_ylim(-2, +2)
    # panel.set_xlim(0, 1000)
    #
    # plt.show()
