# %%
import qiskit as q
from matplotlib import style
from qiskit import QuantumCircuit
from qiskit import Aer
from qiskit import ClassicalRegister
from qiskit.visualization import plot_histogram
from qiskit import execute
style.use("dark_background")


def execute_circuit(QuantumCircuit):
    simulator = Aer.get_backend('qasm_simulator')
    result = execute(QuantumCircuit, simulator, shots=1024).result()
    results = result.get_counts(QuantumCircuit)
    circuit_diagram = QuantumCircuit.draw()
    histogram = plot_histogram(results)
    return results, circuit_diagram, histogram


