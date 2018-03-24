import random
import pyrosim
import matplotlib.pyplot as plt
from robot import ROBOT
from individual import INDIVIDUAL


for i in range(0, 10):

    individual = INDIVIDUAL()

    individual.evaluate()



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

