import QuantumSketchBook as QSB


with QSB.Context(-10, 10, 0.01, 0, 2, 1):
    gaussian = QSB.gaussian_state(0, 3, 0)  # 平均0, 波動関数の標準偏差3, 波数0 のGauss型波束
    QSB.plot(gaussian, title="GAUSS")

    print(gaussian.random_values(5))
    # -->  [-1.6  -0.15  1.1   0.18 -1.4 ]
