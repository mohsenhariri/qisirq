from os import getenv

import qiskit
from qiskit import *
from qiskit_ibm_provider import IBMProvider, accounts

ibm_token = getenv("IBMTOKEN")
if ibm_token is None:
    raise Exception("need a token.")

# try:
#     IBMProvider.save_account(token=ibm_token)
# except accounts.exceptions.AccountAlreadyExistsError as msg:
#     print(msg)
# except Exception as err:
#     raise err


qr = QuantumRegister(2)

cr = ClassicalRegister(2)

circuit = QuantumCircuit(qr, cr)

import matplotlib
import matplotlib.pyplot as plt

print(circuit.draw())

circuit.h(qr[0])
circuit.draw(output="mpl")
plt.show()
plt.savefig("fds.png")
