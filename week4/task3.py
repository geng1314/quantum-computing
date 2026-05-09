from qiskit import QuantumCircuit
from qiskit.visualization import plot_state_qsphere, plot_histogram
import matplotlib.pyplot as plt
import numpy as np


qc = QuantumCircuit(2, 2)
qc.h(0)
qc.cx(0,1)
qc.measure_all()

qc.draw("mpl")  
plt.show()