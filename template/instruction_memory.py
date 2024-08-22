from lib import memory, component

MEMORY_SIZE = 1024

class instruction_memory(memory):
    def __init__(self, size):
        super().__init__(size)
        self.tail = 0

    def write_instruction(self, instruction):
        self.write_word(self.tail, instruction)
        self.tail += 4

    def read_instruction(self, address):
        return self.read_word(address)

class c_instr_memory(component):
    def __init__(self):
        super().__init__()
        self.mem = instruction_memory(MEMORY_SIZE)
        self.mem.name = "INSTR"
        self.fatal_exceptions.append("EOF")
        self.data.add_value("IR", 0)

    def setup(self, pc):
        self.add_dependency(pc)

    def _compute(self):
        super()._compute()
        address = self.input['address']

        try:
            self.data.update_value("IR", self.mem.read_instruction(address))
        except Exception as e:
            self.data.clean()
            self.data.update_dependents()
            raise e
