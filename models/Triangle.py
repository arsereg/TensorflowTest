import math


class Triangle:
    def __init__(self, catetoUno:float, catetoDos: float):
        self.catetoUno = catetoUno
        self.catetoDos = catetoDos


    def hipotenusa(self):
        return math.sqrt(self.catetoUno**2 + self.catetoDos**2)

    def to_dict(self):
        return {
            "catetoUno": self.catetoUno,
            "catetoDos": self.catetoDos,
            "hipotenusa": self.hipotenusa()
        }