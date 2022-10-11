class Output:
    def __init__(self, field, is_hexagonal):
        self.field = field
        self.is_hexagonal = is_hexagonal

    def get_solution(self, solution):
        result = []
        passed_middle = False
        for i in range(self.field.height):
            line = []
            next_line = []
            width = len(self.field.field[i])
            if not passed_middle:
                passed_middle = (width == self.field.width)
            if self.is_hexagonal:
                self.align_center(line, next_line, width, passed_middle)
            for j in range(width):
                line.append(self.field.field[i][j])
                line.append(self.get_horizontal_connection(i, j, solution))
                if self.is_hexagonal:
                    next_line.append(
                        self.get_diagonal_connection(i, j, solution, passed_middle))
                else:
                    next_line.append(
                        self.get_vertical_connection(i, j, solution))
            result.append(line)
            if i < self.field.height - 1:
                result.append(next_line)
        return result

    def show_solutions(self, solutions):
        any_solutions = False
        for i, solution in enumerate(solutions):
            any_solutions = True
            print('Решение {}'.format(i + 1))
            self.print_solution(self.get_solution(solution))
        if not any_solutions:
            print('Нет решений')

    @staticmethod
    def print_solution(solution):
        for i in range(len(solution)):
            print(''.join(solution[i]))

    @staticmethod
    def get_horizontal_connection(i, j, solution):
        if [(i, j), (i, j + 1)] in solution:
            return '---'
        return ' ' * 3

    @staticmethod
    def get_vertical_connection(i, j, solution):
        if [(i, j), (i + 1, j)] in solution:
            return '|' + ' ' * 3
        return ' ' * 4

    @staticmethod
    def get_diagonal_connection(i, j, solution, passed_middle):
        if not passed_middle:
            if [(i, j), (i + 1, j)] in solution:
                return '/' + ' ' * 3
            elif [(i, j), (i + 1, j + 1)] in solution:
                return ' ' * 2 + '\\' + ' '
        else:
            if [(i, j), (i + 1, j)] in solution:
                if j == 0:
                    return '\\' + ' '
                return ' ' * 2 + '\\' + ' '
            elif [(i, j), (i + 1, j - 1)] in solution:
                return '/' + ' ' * 3
        if passed_middle and j == 0:
            return ' ' * 2
        return ' ' * 4

    def align_center(self, line, next_line, width, passed_middle):
        margin = 2 * (self.field.width - width)
        line.append(' ' * margin)
        if not passed_middle:
            next_line.append(' ' * (margin - 1))
        else:
            next_line.append(' ' * (margin + 1))
