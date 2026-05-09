from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_state_qsphere, plot_histogram
import matplotlib.pyplot as plt
import random
import numpy as np


qc3 = QuantumCircuit(2, 2)
qc3.h(0)
qc3.cx(0,1)
qc3.measure_all()

qc3.draw("mpl")  
plt.show()