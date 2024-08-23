from lib import memory, component
from .intermediate_registers import ex_mem

MEMORY_SIZE = 1024

class c_data_memory(component):
    def __init__(self):
        self.mem = memory(MEMORY_SIZE)
        self.mem.name = "RAM"
        super().__init__()
        self.data.add_value("LMD", 0)

    def setup(self):
        self.add_dependency(ex_mem())

    def _compute(self):
        super()._compute()
        data = self.input['EX_MemData']
        address = self.input['EX_ALUResult']

        if self.input['EX_MemWrite'] == 1:
            self.mem.write_word(address, data)
        if self.input['EX_MemRead'] == 1:
            try:
                self.data.update_value("LMD", self.mem.read_word(address).value)
            except:
                self.data.update_value("LMD", self.mem.read_word(address))

