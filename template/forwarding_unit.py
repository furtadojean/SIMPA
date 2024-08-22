from lib import component
from .intermediate_registers import id_ex, ex_mem, mem_wb

class forwarding_unit(component):
    def __init__(self):
        super().__init__()
        self.data.add_value("ForwardA", 'ID')
        self.data.add_value("ForwardB", 'ID')

    def setup(self):
        self.add_dependency(id_ex())
        self.add_dependency(ex_mem())
        self.add_dependency(mem_wb())

    def _compute(self):
        super()._compute()
        #print(self.input.input)
        self.data.update_value("ForwardA", 'ID')
        self.data.update_value("ForwardB", 'ID')
        if self.input['EX_RegWrite'] == 1 and \
                self.input['EX_IR'].rd != 'zero' and \
                self.input['EX_IR'].rd == self.input['ID_IR'].rs1:
                    self.data.update_value("ForwardA", 'EX')
        elif self.input['MEM_RegWrite'] == 1 and \
                self.input['MEM_IR'].rd != 'zero' and \
                self.input['MEM_IR'].rd == self.input['ID_IR'].rs1:
                    self.data.update_value("ForwardA", 'MEM')
        if self.input['EX_RegWrite'] == 1 and \
                self.input['EX_IR'].rd != 'zero' and \
                self.input['EX_IR'].rd == self.input['ID_IR'].rs2:
                    self.data.update_value("ForwardB", 'EX')
        elif self.input['MEM_RegWrite'] == 1 and \
                self.input['MEM_IR'].rd != 'zero' and \
                self.input['MEM_IR'].rd == self.input['ID_IR'].rs2:
                    self.data.update_value("ForwardB", 'MEM')
        #print("Forwarding Unit", self.data.data)
