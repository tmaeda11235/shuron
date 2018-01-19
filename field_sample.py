import QuantumSketchBook as QSB
from QuantumSketchBook.field import Field


with QSB.Context(0, 2, 1, 0, 2, 1) as mesh:
    print(mesh.x_vector)
    # --> [0 1]

    function_field = Field(lambda x: x + 1)  # 引数が関数の場合
    print(function_field.vector)
    # --> [1 2]

    list_field = Field([1, 2])  # 引数がlistの場合
    print(list_field.vector)
    # --> [1 2]

    generator_field = Field(x + 1 for x in range(2))  # iterableならば受け取ることができる
    print(generator_field.vector)
    # --> [1 2]

    wrong_length = Field([1, 2, 3]) #  要素数が合わない場合はValueErrorが送出される
    # --> ValueError: Length of input iterable must be equal to mesh.num

