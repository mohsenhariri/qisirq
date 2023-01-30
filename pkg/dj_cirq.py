# import cirq

# circuit = cirq.Circuit()

# (q0, q1) = cirq.LineQubit.range(2)

# circuit.append([cirq.H(q0), cirq.CNOT(q0, q1)])
# circuit.append([cirq.measure(q0), cirq.measure(q1)])

# print(circuit)

# sim = cirq.Simulator()
# results = sim.run(circuit, repetitions=10)
# print(results)

import cirq
import matplotlib.pyplot as plt
import numpy as np

# import cirq_google
# print(cirq_google.Sycamore)


a = cirq.NamedQubit("a")
b = cirq.NamedQubit("b")
c = cirq.NamedQubit("c")

operations = [cirq.H(a), cirq.H(b), cirq.CNOT(b, c), cirq.H(b)]

circuit1 = cirq.Circuit(operations)

# print("circuit1: ", circuit1)

circuit2 = cirq.Circuit()

qubits = [cirq.NamedQubit(f"{i}") for i in range(4)]


ops1 = [cirq.H(qubits[0]), cirq.H(qubits[1])]
ops2 = [cirq.CNOT(qubits[1], qubits[2]), cirq.CNOT(qubits[0], qubits[3])]
ops3 = [cirq.H(qubits[1])]

circuit2.append(ops1)
circuit2.append(ops2)
circuit2.append(ops3)

# circuit2.append([ops1, ops2, ops3])

print("circuit2\n", circuit2)


print(cirq.unitary(cirq.H))


for i, moment in enumerate(circuit2):
    print(f"Moment {i}: \n{moment}")

print(repr(circuit2))