# from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
# from numpy import pi

# qreg_q = QuantumRegister(3, 'q')
# creg_c = ClassicalRegister(3, 'c')

# circuit = QuantumCircuit(qreg_q, creg_c)

# circuit.reset(qreg_q[0])
# circuit.reset(qreg_q[1])
# circuit.reset(qreg_q[2])
# circuit.h(qreg_q[0])
# circuit.h(qreg_q[1])
# circuit.h(qreg_q[2])
# circuit.z(qreg_q[0])
# circuit.cz(qreg_q[1], qreg_q[2])
# circuit.h(qreg_q[0])
# circuit.h(qreg_q[1])
# circuit.h(qreg_q[2])
# circuit.measure(qreg_q[0], creg_c[0])
# circuit.measure(qreg_q[1], creg_c[1])
# circuit.measure(qreg_q[2], creg_c[2])

# print(circuit.draw())

import ibm_token
import matplotlib.pyplot as plt
import numpy as np

# importing Qiskit
from qiskit import IBMQ, Aer, QuantumCircuit, QuantumRegister, transpile
from qiskit.providers.ibmq import least_busy
from qiskit.visualization import plot_histogram


def cplot(circuit):
    circuit.draw("mpl")
    plt.show()


n = 3


def oracle():
    const_oracle_circuit = QuantumCircuit(n + 1)

    output = np.random.randint(2)
    if output == 1:
        const_oracle_circuit.x(n)

    print("const oracle", const_oracle_circuit.draw())

    balanced_oracle_circuit = QuantumCircuit(n + 1)
    b_str = "101"

    for qubit in range(len(b_str)):
        if b_str[qubit] == "1":
            balanced_oracle_circuit.x(qubit)

    balanced_oracle_circuit.barrier()

    for qubit in range(n):
        balanced_oracle_circuit.cx(qubit, n)

    balanced_oracle_circuit.barrier()

    for qubit in range(len(b_str)):
        if b_str[qubit] == "1":
            balanced_oracle_circuit.x(qubit)

    print(balanced_oracle_circuit)
    return balanced_oracle_circuit


balanced_oracle_circuit = oracle()


dj_circuit = QuantumCircuit(n + 1, n)

# Apply H-gates
for qubit in range(n):
    dj_circuit.h(qubit)

# Put qubit in state |->
dj_circuit.x(n)
dj_circuit.h(n)
print(dj_circuit.draw())

dj_circuit = QuantumCircuit(n + 1, n)

# Apply H-gates
for qubit in range(n):
    dj_circuit.h(qubit)

# Put qubit in state |->
dj_circuit.x(n)
dj_circuit.h(n)

# Add oracle
dj_circuit = dj_circuit.compose(balanced_oracle_circuit)
print(dj_circuit.draw())
# dj_circuit.draw('mpl')
# plt.show()

# Repeat H-gates
for qubit in range(n):
    dj_circuit.h(qubit)
dj_circuit.barrier()

# Measure
for i in range(n):
    dj_circuit.measure(i, i)


cplot(dj_circuit)


# use local simulator
aer_sim = Aer.get_backend("aer_simulator")
results = aer_sim.run(dj_circuit).result()
answer = results.get_counts()

plot_histogram(answer)
plt.show()



connection = ibm_token.Connection()
backend = connection.connect(2)


from qiskit.tools.monitor import job_monitor

transpiled_dj_circuit = transpile(dj_circuit, backend, optimization_level=3)
job = backend.run(transpiled_dj_circuit)
job_monitor(job, interval=2)


results = job.result()
answer = results.get_counts()

plot_histogram(answer)
plt.show()
