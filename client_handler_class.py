from instance_class import *
from input_class import *
from output_class import *


class ClientUI:
    def __init__(self):
        self.input = Input()
        self.output = None

    def get_instance(self):
        is_hexagonal, file_name = self.input.get_data()
        field = self.input.get_field(file_name, is_hexagonal)
        self.output = Output(field, is_hexagonal)
        return Instance(field, is_hexagonal)

    def show_solutions(self, solutions):
        self.output.show_solutions(solutions)
