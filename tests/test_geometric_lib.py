import unittest
import geometric_lib as gl

class CircleTestCase(unittest.TestCase):

    def test_perimeter_correctness(self):
        test_data = [
            [10, 62.83185307179586],
            [100000000000, 628318530717.958647693],
            [2.5, 15.707963267948966],
            [0, 0],
            [0.001, 0.006283185307179587]
        ]
        for i in test_data:
            param = gl.circle.perimeter(i[0])
            expected = i[1]
            with self.subTest():
                self.assertAlmostEqual(param, expected)

    def test_area_correctness(self):
        test_data = [
            [10, 314.1592653589793],
            [100000000000, 3.141592653589793e+22],
            [2.5, 19.634954084936208],
            [0, 0],
            [0.001, 3.1415926535897933e-06]
        ]
        for i in test_data:
            param = gl.circle.area(i[0])
            expected = i[1]
            with self.subTest():
                self.assertAlmostEqual(param, expected)

class RectangleTestCase(unittest.TestCase):

    def test_perimeter_correctness(self):
        test_data = [
            [4.5, 5.5, 20.0],
            [10, 2, 24],
            [100000000000, 3, 200000000006],
            [0, 5, 10],
            [0.001, 0.002, 0.006]
        ]
        for i in test_data:
            param = gl.rectangle.perimeter(i[0], i[1])
            expected = i[2]
            with self.subTest():
                self.assertAlmostEqual(param, expected)

    def test_area_correctness(self):
        test_data = [
            [4.5, 5.5, 24.75],
            [10, 2, 20],
            [100000000000, 3, 300000000000],
            [0, 5, 0],
            [0.001, 0.002, 2e-06]
        ]
        for i in test_data:
            param = gl.rectangle.area(i[0], i[1])
            expected = i[2]
            with self.subTest():
                self.assertAlmostEqual(param, expected)


class SquareTestCase(unittest.TestCase):

    def test_perimeter_correctness(self):
        test_data = [
            [2.3, 9.2],
            [10, 40],
            [100000000000, 400000000000],
            [0, 0],
            [0.001, 0.004]
        ]
        for i in test_data:
            param = gl.square.perimeter(i[0])
            expected = i[1]
            with self.subTest():
                self.assertAlmostEqual(param, expected)

    def test_area_correctness(self):
        test_data = [
            [2.3, 5.289999999999999],
            [10, 100],
            [100000000000, 10000000000000000000000],
            [0, 0],
            [0.001, 1e-06]
        ]
        for i in test_data:
            param = gl.square.area(i[0])
            expected = i[1]
            with self.subTest():
                self.assertAlmostEqual(param, expected)


class TriangleTestCase(unittest.TestCase):

    def test_perimeter_correctness(self):
        test_data = [
            [2, 2, 2, 6],
            [3, 4, 5, 12],
            [2.5, 3.5, 4.5, 10.5],
            [100000000000, 100000000000, 100000000000, 300000000000],
            [0, 0, 0, 0],
            [0.001, 0.002, 0.003, 0.006]
        ]
        for i in test_data:
            param = gl.triangle.perimeter(i[0], i[1], i[2])
            expected = i[3]
            with self.subTest():
                self.assertAlmostEqual(param, expected)

    def test_area_correctness(self):
        test_data = [
            [2.3, 2.2, 2.53],
            [10, 4, 20],
            [100000000000, 100000000000, 5e+21],
            [0, 5, 0],
            [0.001, 0.002, 1e-06]
        ]
        for i in test_data:
            param = gl.triangle.area(i[0], i[1])
            expected = i[2]
            with self.subTest():
                self.assertAlmostEqual(param, expected)


