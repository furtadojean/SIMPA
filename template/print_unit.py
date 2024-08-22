from lib import component
from .intermediate_registers import ex_mem

import io
from contextlib import redirect_stdout

class print_unit(component):
    def __init__(self):
        super().__init__()
        self.buffer = ""

    def setup(self, data_memory, registers):
        self.add_dependency(ex_mem())
        self.data_memory = data_memory
        self.registers = registers

    def _compute(self):
        super()._compute()
        with io.StringIO() as buf, redirect_stdout(buf):
            if self.input['EX_Print'] == 1:
                if self.input['EX_IR'].instr == 'pint':
                    #print("PINT", self.input['EX_IR'].rs1, self.input['EX_ALUResult'])
                    try:
                        print(self.registers[self.input['EX_IR'].rs1])
                    except:
                        print("PINT", None)
                elif self.input['EX_IR'].instr == 'pstr':
                    try:
                        print(self.data_memory.read_word(self.input['EX_ALUResult']).value)
                    except:
                        print("PSTR", None)
            self.buffer += buf.getvalue()
