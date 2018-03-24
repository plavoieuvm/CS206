import pyrosim
import matplotlib.pyplot as plt

sim = pyrosim.Simulator(eval_time=1000, play_paused=False)

# Create objects

whiteObject = sim.send_cylinder(x=0, y=0, z=0.6, length=1.0, radius=0.1)

redObject = sim.send_cylinder(x=0, y=0.5, z=1.1, r1=0, r2=1, r3=0, length=1.0, radius=0.1, r=1, g=0, b=0)

# Create joint

joint = sim.send_hinge_joint(first_body_id=whiteObject, second_body_id=redObject, x=0, y=0, z=1.1, n1=-1, n2=0, n3=0,
                             lo=-3.14159/2, hi=3.14159/2)


# Sensors

T0 = sim.send_touch_sensor(body_id=whiteObject)
T1 = sim.send_touch_sensor(body_id=redObject)
P2 = sim.send_proprioceptive_sensor(joint_id=joint)

# Pointing out from tip
R3 = sim.send_ray_sensor(body_id=redObject, x=0, y=1.1, z=1.1, r1=0, r2=1, r3=0)

# Middle pointing down
# R3 = sim.send_ray_sensor(body_id=redObject, x=0, y=0.5, z=1.1, r1=0, r2=0, r3=-1)


# Neurons

SN0 = sim.send_sensor_neuron(sensor_id=T0)
SN1 = sim.send_sensor_neuron(sensor_id=T1)

MN2 = sim.send_motor_neuron(joint_id=joint)

# Synapses

sim.send_synapse(source_neuron_id=SN0, target_neuron_id=MN2, weight=-1.0)

sim.send_synapse(source_neuron_id=SN1, target_neuron_id=MN2, weight=-1.0)





# Start

sim.start()

sim.wait_to_finish()

# Analyze sensor data

sensorData = sim.get_sensor_data(sensor_id=P2)

print(sensorData)

f = plt.figure()

panel = f.add_subplot(111)

plt.plot(sensorData)

panel.set_ylim(-2, +2)
panel.set_xlim(0, 1000)


plt.show()

