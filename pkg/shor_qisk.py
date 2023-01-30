from qiskit import Aer, QuantumCircuit, execute
from qiskit.algorithms import Shor
from qiskit.tools.visualization import plot_histogram
from qiskit.utils import QuantumInstance

backend = Aer.get_backend("qasm_simulator")

q_instance = QuantumInstance(backend, shots=1000)

shor = Shor(N=15, a=2, quantum_instance=q_instance)

Shor.run(shor)
