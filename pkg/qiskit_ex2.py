import qiskit.quantum_info as qi
from qiskit.circuit.library import FourierChecking
from qiskit.visualization import plot_histogram

f = [1, -1, -1, -1]
g = [1, 1, -1, -1]

circ = FourierChecking(f=f, g=g)
print(circ.draw())
