from models.Triangle import Triangle
import random

class TriangleFactory:


    def __create(self, catetoUno:float, catetoDos: float):
        return Triangle(catetoUno=catetoUno, catetoDos=catetoDos)

    def __createRandom(self):
        return Triangle(catetoUno= random.randint(1, 100), catetoDos=random.randint(1, 100))

    def createTriangles(self, n: int):
        triangles = []
        for i in range(n):
            triangles.append(self.__createRandom())
        return triangles