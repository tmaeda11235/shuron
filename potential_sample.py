import QuantumSketchBook as QSB


with QSB.Context(-10, 10, 0.01, 0, 2, 1):
    step_potential = QSB.step(5, 0)
    QSB.plot(step_potential, title="STEP")  # ステップポテンシャル

    box_potential = QSB.box(2, 1, 4)
    QSB.plot(box_potential, title="BOX")  # 箱型ポテンシャル

    complex_potential = step_potential + box_potential
    QSB.plot(complex_potential, title="COMPLEX")  # ポテンシャルの足し合わせ

    square_potential = QSB.Potential(lambda x: x ** 2)
    QSB.plot(square_potential, title="SQUARE")  # 2次関数

    QSB.plot(QSB.kp(1, 2, 1), title="Kronig-Penny")  # Kronig-Pennyポテンシャル
    QSB.plot(QSB.vacuum_kp(1, 2, 1), title="vacuum_and_Kronig-Penny")  # 真空とKronig-Pennyポテンシャル
