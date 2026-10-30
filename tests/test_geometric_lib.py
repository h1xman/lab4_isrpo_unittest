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
                self.assertEqual(param, expected)

    def test_area_correcttness(self):
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
                self.assertEqual(param, expected)

    def test_input_correctness(self):
        test_data = [
            -10,
            -100000000000,
            -2.5,
            -0.001
        ]        
        for i in test_data:
            param_area = gl.circle.area(i)
            param_perimeter = gl.circle.perimeter(i)
            with self.subTest():
                self.assertIsNot(type(param_area), float)
                self.assertIsNot(type(param_perimeter), float)


