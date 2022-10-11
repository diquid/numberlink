from solver_class import *
from client_handler_class import *


def main():
    cui = ClientUI()
    instance = cui.get_instance()
    solver = Solver(instance)
    solutions = solver.solve()
    cui.show_solutions(solutions)


if __name__ == '__main__':
    main()
