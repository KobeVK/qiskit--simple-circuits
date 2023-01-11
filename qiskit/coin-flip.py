# %%
import qiskit as q
from matplotlib import style
from qiskit import QuantumCircuit
from qiskit import Aer
from qiskit import ClassicalRegister
from qiskit.visualization import plot_histogram
from qiskit import execute
style.use("dark_background")

circuit = q.QuantumCircuit(2,2)
circuit.h(0)
circuit.cx(0,1)

circuit.measure(0,0)
circuit.measure(1,1)


circuit.draw(output='mpl')

backend = Aer.get_backend('qasm_simulator')
job=execute(circuit, backend, shots=1024)
job_result = job.result()
results = job_result.get_counts(circuit)
plot_histogram(results)


# %%



