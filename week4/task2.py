from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_state_qsphere, plot_histogram
import matplotlib.pyplot as plt
import numpy as np


qasm = """
OPENQASM 2.0;
include "qelib1.inc";
qreg q[2];
creg c[2];
h q[0];
cx q[0],q[1];
measure q->c;
"""

qc2 = QuantumCircuit.from_qasm_str(qasm)
print(qc2)

result = AerSimulator().run(qc2, shots=100).result()
plot_histogram(result.get_counts())
plt.show()