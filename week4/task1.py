from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_state_qsphere, plot_histogram
import matplotlib.pyplot as plt
import numpy as np


qc1 = QuantumCircuit(2)
qc1.h(0)
qc1.p(np.pi/2, 0) 

qc1.draw("mpl")
plt.show()

sim = AerSimulator(method="statevector")
qc1.save_statevector()
state = sim.run(qc1).result().get_statevector()

plot_state_qsphere(state)
plt.show()