#!/usr/bin/env python3
#%%
from turtle import back
from unittest import result
import qiskit as q
from qiskit import IBMQ
%matplotlib inline

circuit = q.QuantumCircuit(2,2)  # 2 qubits, 2 classical bits 
circuit.x(0) # "x" is a "not" gate. It flips the value. Starting value is a 0, so this flips to a 1. 
circuit.cx(0, 1) #cnot, controlled not, Flips 2nd qubit's value if first qubit is 1
circuit.measure([0,1], [0,1])  # ([qbitregister], [classicalbitregister]) Measure qubit 0 and 1 to classical bits 0 and 1
circuit.draw()

IBMQ.save_account(open("ibm_token.txt","r").read())
IBMQ.load_account()
IBMQ.providers()
provider = IBMQ.get_provider("ibm-q")

#function to know how many queued qbuts in each provider
for backend in provider.backends():
    try:
        qubit_count = len(backend.properties().qubits)
    except:
        qubit_count = "simulated"
        
    print(f"{backend.name()} has {backend.status().pending_jobs} queued and {qubit_count} qubits")

#function to tell us where we are on the queue 
from qiskit.tools.monitor import job_monitor

backend = provider.get_backend("ibmq_belem")
job = q.execute(circuit, backend=backend, shots=1024)
job_monitor(job)

from qiskit.visualization import plot_histogram
from matplotlib import style

style.use("dark_background")
result = job.result()
counts = result.get_counts(circuit)

plot_histogram([counts])




# %%
