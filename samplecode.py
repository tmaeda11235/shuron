import QuantumSketchBook as QSB
with QSB.Context(-5, 5, 0.01, 0, 5, 0.01) as mesh:
     my_potential = QSB.potential(lambda x: 1 / 2 * x ** 2)
     my_state = QSB.gaussian_state(0, 2, 0.5)
     my_hamiltonian = QSB.Hamiltonian(my_potential)
     my_schroedinger = QSB.Schroedinger(my_hamiltonian,  my_state)
     QSB.plot(my_schroedinger, False, True, "sample_code")