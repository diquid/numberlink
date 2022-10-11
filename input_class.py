import argparse
from field_class import *
import math
import sys


sys.tracebacklimit = 0


class Input:
    def get_field(self, file_name, is_hexagonal):
        if is_hexagonal:
            return self.get_hexagonal_field(file_name)
        return self.get_rectangle_field(file_name)

    def get_hexagonal_field(self, file_name):
        with open(file_name) as file:
            line = file.readline().split()
            self.check_line(line)
            self.check_params_hexagon(line)
            height = int(line[0])
            field = []
            max_width = 2 + math.floor(height / 2)
            self.get_field_half(math.ceil(height / 2), file, 2, 1, field)
            self.get_field_half(
                math.ceil(height / 2) - 1, file, max_width - 1, -1, field)
            return Field((max_width, height), field)

    def get_field_half(self, num_of_lines, file, width, delta, field):
        for i in range(num_of_lines):
            line = file.readline().split()
            self.check_line_width(line, width)
            width += delta
            field.append(line)

    @staticmethod
    def check_params_hexagon(line):
        if len(line) > 1 or int(line[0]) <= 0:
            raise ValueError(
                'Ожидалось одно положительное целое число - '
                'высота 6-угольного поля')

    def get_rectangle_field(self, file_name):
        with open(file_name) as file:
            line = file.readline().split()
            self.check_line(line)
            self.check_params_rectangle(line)
            width, height = map(int, line)
            field = []
            for line in file:
                line = line.split()
                self.check_line(line)
                self.check_line_width(line, width)
                field.append(line)
            return Field((width, height), field)

    @staticmethod
    def check_params_rectangle(line):
        if len(line) < 2 or int(line[0]) <= 0 or int(line[1]) <= 0:
            raise ValueError(
                'Ожидалось два положительных целых числа через пробел - '
                'ширина и высота поля')

    @staticmethod
    def check_line(line):
        if not line:
            raise ValueError('Пустая строка')

    @staticmethod
    def check_line_width(line, width):
        if len(line) > width:
            raise ValueError('Количество символов больше ширины поля')
        if len(line) < width:
            raise ValueError('Количество символов меньше ширины поля"')

    @staticmethod
    def get_data():
        parser = argparse.ArgumentParser()
        parser.add_argument('-s', '--hexagonal', help='6-угольное поле '
                                                      '(по умолчанию '
                                                      'прямоугольное)',
                            action='store_true', default=False)
        parser.add_argument("file_name",
                            help="имя или путь к файлу с головоломкой. ДЛЯ "
                                 "6-УГОЛЬНОГО ПОЛЯ в первой строке одно целое "
                                 "положительное число i - высота поля. Далее "
                                 "в следующих i строках содержатся строки "
                                 "поля - j элементов поля через пробел, где "
                                 "j - сначала увеличивающаяся, затем "
                                 "уменьшающаяся ширина строки. Например, "
                                 "в 6-угольном поле высоты 3 длины строк "
                                 "будут равны 2, 3, 2. # - пустая клетка. "
                                 "Можно использовать любой из примеров в "
                                 "examples/(номер от 1 до 4)_h.txt. "
                                 "ДЛЯ ПРЯМОУГОЛЬНОГО ПОЛЯ: в первой строке "
                                 "два целых положительных числа j, i - высота "
                                 "и ширина поля. Далее в следующих i строках "
                                 "содержатся строки поля - j элементов поля "
                                 "через пробел, где j - ширина поля. # - "
                                 "пустая клетка. Можно использовать любой из "
                                 "примеров в examples/(номер от 1 до 7).txt",
                            type=str)
        args = parser.parse_args()
        return args.hexagonal, args.file_name
