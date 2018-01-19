import QuantumSketchBook as QSB


with QSB.Context(-40, 40, 0.05, 0, 60, 0.05):
    initial_state = QSB.gaussian_state(0, 8, 1)
    free_particle = QSB.potential(lambda x: 0 * x)

    free_boundary = QSB.Hamiltonian(free_particle, boundary="free")
    schroedinger = QSB.Schroedinger(free_boundary, initial_state)
    QSB.plot(schroedinger, title="free_boundary", save=True)  # 自由端境界条件

    fix_boundary = QSB.Hamiltonian(free_particle, boundary="fix")
    schroedinger = QSB.Schroedinger(fix_boundary, initial_state)
    QSB.plot(schroedinger, title="fix_boundary", save=True)  # 固定端境界条件

    periodic_boundary = QSB.Hamiltonian(free_particle, boundary="period")
    schroedinger = QSB.Schroedinger(periodic_boundary, initial_state)
    QSB.plot(schroedinger, title="periodic_boundary", save=True)  # 周期境界条件

    square_potential = QSB.potential(lambda x: 0.003 * x ** 2)
    hamiltonian = QSB.Hamiltonian(square_potential)
    schroedinger = QSB.Schroedinger(hamiltonian, initial_state)
    QSB.plot(schroedinger, title="square_potential", save=True)
