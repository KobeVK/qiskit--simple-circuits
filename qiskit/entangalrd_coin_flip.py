# %%
import qiskit as q
#from matplotlib import style
from qiskit import QuantumCircuit
from qiskit import Aer
from qiskit import ClassicalRegister
from qiskit.visualization import plot_histogram
from qiskit.visualization import plot_bloch_multivector
from qiskit import execute
style.use("dark_background")

circuit = q.QuantumCircuit(1)

backend = Aer.get_backend('stateVectorSimulator')
result = execute(q, backend).result()
stateVectorResult = result.get_stateVector(q)

circuit.draw(output='mpl')
plot_bloch_statevector(stateVectorResult)


# %%



