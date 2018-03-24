import pyrosim
import matplotlib.pyplot as plt


class ROBOT:

    def __init__(self, sim, wts):

        self.whiteObject = sim.send_cylinder(x=0, y=0, z=0.6, length=1.0, radius=0.1)

        self.redObject = sim.send_cylinder(x=0, y=0.5, z=1.1, r1=0, r2=1, r3=0, length=1.0, radius=0.1, r=1, g=0, b=0)

        # Create joint

        self.joint = sim.send_hinge_joint(first_body_id=self.whiteObject, second_body_id=self.redObject, x=0, y=0,
                                          z=1.1, n1=-1, n2=0, n3=0, lo=-3.14159 / 2, hi=3.14159 / 2)

        # Sensors

        self.T0 = sim.send_touch_sensor(body_id=self.whiteObject)
        self.T1 = sim.send_touch_sensor(body_id=self.redObject)

        self.P2 = sim.send_proprioceptive_sensor(joint_id=self.joint)

        self.P4 = sim.send_position_sensor(body_id=self.redObject)

        # Pointing out from tip
        self.R3 = sim.send_ray_sensor(body_id=self.redObject, x=0, y=1.1, z=1.1, r1=0, r2=1, r3=0)

        # Middle pointing down
        # R3 = sim.send_ray_sensor(body_id=redObject, x=0, y=0.5, z=1.1, r1=0, r2=0, r3=-1)

        # Neurons

        self.SN0 = sim.send_sensor_neuron(sensor_id=self.T0)
        self.SN1 = sim.send_sensor_neuron(sensor_id=self.T1)
        self.SN2 = sim.send_sensor_neuron(sensor_id=self.T1)
        self.SN3 = sim.send_sensor_neuron(sensor_id=self.T1)
        self.MN1 = sim.send_motor_neuron(joint_id=self.joint)

        motorNeurons = {}
        motorNeurons[0] = self.MN1


        sensorNeurons = {}
        sensorNeurons[0] = self.SN0
        sensorNeurons[1] = self.SN1
        sensorNeurons[2] = self.SN2
        sensorNeurons[3] = self.SN3

        # Synapses

        for s in sensorNeurons:

            for m in motorNeurons:

                sim.send_synapse(source_neuron_id=sensorNeurons[s], target_neuron_id=motorNeurons[m], weight=wts[s])
