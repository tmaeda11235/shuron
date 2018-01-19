import QuantumSketchBook as QSB


with QSB.Context(-10, 10, 0.1, 0, 10, 0.1) as mesh:
    print(mesh.__class__)
    # --> <class 'QuantumSketchBook.mesh.Mesh'>

    print(mesh.x_num)
    # --> 200

    print(mesh.t_num)
    # --> 100

    print(mesh.x_vector)
    # -->[ -1.00000000e+01  -9.90000000e+00  -9.80000000e+00  -9.70000000e+00 ...]
