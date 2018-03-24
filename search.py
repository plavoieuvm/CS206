import random
import pyrosim
import matplotlib.pyplot as plt
from robot import ROBOT


for i in range(0, 10):

    sim = pyrosim.Simulator(eval_time=1000, play_paused=False)

    wt = random.random()*2-1

    robot = ROBOT(sim, wt)

    print(wt)

    # Start

    sim.start()

    sim.wait_to_finish()

# Analyze sensor data

# sensorData = sim.get_sensor_data(sensor_id=P2)
#
# print(sensorData)
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
#
# plt.show()

