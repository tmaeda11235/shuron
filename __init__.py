from QuantumSketchBook.context import Context
from QuantumSketchBook.state import State, gaussian_state
from QuantumSketchBook.potential import Potential, potential, free,  box, kp, step, vacuum_kp, kp_vacuum
from QuantumSketchBook.hamiltonian import Hamiltonian
from QuantumSketchBook.schroedinger import Schroedinger


def plot(plotted, show=True, save=False, title="no_title", *args, **kwargs):
    return plotted.__plot__(show, save, title, *args, **kwargs)
