import os
import sys
import unittest
from instance_class import *
from solver_class import *
from input_class import *
from output_class import *


sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             os.path.pardir))


class TestInstanceGeneration(unittest.TestCase):
    def test_no_pair_error(self):
        with self.assertRaises(Exception) as context:
            field = Field((3, 3), [['1', '*', '*'],
                                   ['2', '*', '2'],
                                   ['*', '*', '*']])
            instance = Instance(field, False)
        self.assertTrue('Нельзя решать головоломку, когда у некоторых чисел нет пары' in str(context.exception))

    def test_excess_numbers_error(self):
        with self.assertRaises(Exception) as context:
            field = Field((3, 3), [['1', '*', '1'],
                                   ['2', '*', '2'],
                                   ['*', '*', '1']])
            instance = Instance(field, False)
        self.assertTrue(
            'Нельзя решать головоломку, когда на поле более двух одинаковых чисел' in str(context.exception))


class TestSolver(unittest.TestCase):
    def test_solve_hexagonal(self):
        input_handler = Input()
        field = input_handler.get_field(
            'C:/Users/acer/OneDrive/Рабочий стол/urfu/python task/numberlink_task/numberlink/input_examples/field_6_hex.txt',
            True)
        instance = Instance(field, True)
        solver = Solver(instance)
        solutions = list(solver.solve())
        assert len(solutions) > 0

    def test_solve_rectangle(self):
        input_handler = Input()
        field = input_handler.get_field(
            'C:/Users/acer/OneDrive/Рабочий стол/urfu/python task/numberlink_task/numberlink/input_examples/field_3.txt',
            False)
        instance = Instance(field, False)
        solver = Solver(instance)
        solutions = list(solver.solve())
        assert len(solutions) > 0

    def test_no_solutions_hexagonal(self):
        input_handler = Input()
        field = input_handler.get_field(
            'C:/Users/acer/OneDrive/Рабочий стол/urfu/python task/numberlink_task/numberlink/input_examples/field_7_hex_wrong.txt',
            True)
        instance = Instance(field, True)
        solver = Solver(instance)
        solutions = list(solver.solve())
        assert len(solutions) == 0

    def test_no_solutions_rectangle(self):
        input_handler = Input()
        field = input_handler.get_field(
            'C:/Users/acer/OneDrive/Рабочий стол/urfu/python task/numberlink_task/numberlink/input_examples/field_5_wrong.txt',
            False)
        instance = Instance(field, False)
        solver = Solver(instance)
        solutions = list(solver.solve())
        assert len(solutions) == 0


class TestFieldParser(unittest.TestCase):
    input_handler = Input()

    def test_params_error_hexagonal(self):
        context = self.setup_test('3 3', '1 2', '* * *', '1 2', is_hexagonal=True)
        self.assertTrue('Ожидалось одно положительное целое число - высота 6-угольного поля' in str(context.exception))

    def test_params_error_rectangle(self):
        context = self.setup_test('2', '1 2', '1 2')
        self.assertTrue('Ожидалось два положительных целых числа через пробел - ширина и высота поля' in str(context.exception))

    def test_width_error_long_hexagonal(self):
        context = self.setup_test('3', '1 2', '* * * *', '1 2', is_hexagonal=True)
        self.assertTrue('Количество символов больше ширины поля' in str(context.exception))

    def test_width_error_small_hexagonal(self):
        context = self.setup_test('3', '1 2', '* *', '1 2', is_hexagonal=True)
        self.assertTrue('Количество символов меньше ширины поля' in str(context.exception))

    def test_width_error_long_rectangle(self):
        context = self.setup_test('2 2', '1 2', '1 2 *')
        self.assertTrue('Количество символов больше ширины поля' in str(context.exception))

    def test_width_error_small_rectangle(self):
        context = self.setup_test('2 2', '1 2', '1')
        self.assertTrue('Количество символов меньше ширины поля' in str(context.exception))

    def setup_file(self, *lines):
        with open('test_file.txt', 'w') as test_file:
            self.write_to_file(test_file, *lines)

    def setup_test(self, *lines, is_hexagonal=False):
        self.setup_file(*lines)
        with self.assertRaises(Exception) as context:
            self.input_handler.get_field('test_file.txt', is_hexagonal)
        return context

    @staticmethod
    def write_to_file(test_file, *lines):
        for line in lines:
            test_file.write(line + '\n')


def space(length):
    return ' ' * length


class TestOutput(unittest.TestCase):
    def test_output_hexagonal(self):
        field = Input().get_field('C:/Users/acer/OneDrive/Рабочий стол/urfu/python task/numberlink_task/numberlink/input_examples/field_8_hex.txt', True)
        output_handler = Output(field, True)
        solution = output_handler.get_solution(list(Solver(
            Instance(field, True)).solve())[0])

        # def space(length):
        #     return ' ' * length

        right = '  \\ '
        left = '/   '
        horizontal = '---'
        expected_output = [
            [space(6), '1', space(3), '2', space(3)],
            [space(5), right, right],
            [space(4), '4', space(3), '*', space(3), '*', space(3)],
            [space(3), right, right, right],
            [space(2), '5', space(3), '*', space(3), '*', space(3), '*', space(3)],
            [space(1), right, right, right, right],
            [space(0), '3', space(3), '5', space(3), '4', space(3), '*', space(3), '*', space(3)],
            [space(1), '\\ ', space(4), space(4), left, left],
            [space(2), '*', horizontal, '3', space(3), '*', space(3), '*', space(3)],
            [space(3), space(2), space(4), left, left],
            [space(4), '*', horizontal, '*', space(3), '*', space(3)],
            [space(5), '\\ ', space(4), left],
            [space(6), '1', space(3), '2', space(3)]]
        self.assertEqual(expected_output, solution)

    def test_output_rectangle(self):
        field = Input().get_field('C:/Users/acer/OneDrive/Рабочий стол/urfu/python task/numberlink_task/numberlink/input_examples/field_9.txt', False)
        output_handler = Output(field, False)
        solution = output_handler.get_solution(list(Solver(
            Instance(field, False)).solve())[0])

        # def space(length):
        #     return ' ' * length

        # 4 3
        # 1 * * 1
        # 2 * 2 3
        # 3 * * *
        vertical = '|   '
        horizontal = '---'
        expected_output = [['2', space(3), '1', horizontal, '*', space(3)],
                           [vertical, space(4), vertical],
                           ['*', horizontal, '2', space(3), '1', space(3)],
                           [space(4), space(4), space(4)],
                           ['3', horizontal, '*', horizontal, '3', space(3)]]
        self.assertEqual(expected_output, solution)


if __name__ == '__main__':
    unittest.main()
