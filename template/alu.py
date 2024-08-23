from lib import component
from .intermediate_registers import id_ex, ex_mem, mem_wb

class ALU(component):
    def __init__(self):
        super().__init__()

    def setup(self, forwarding_unit):
        self.add_dependency(id_ex())
        self.add_dependency(ex_mem())
        self.add_dependency(mem_wb())
        self.add_dependency(forwarding_unit)

    def _compute(self):
        super()._compute()
        A = self.input['ID_A']
        B = self.input['ID_B']
        if self.input['ForwardA'] == 'EX':
            A = self.input['EX_ALUResult']
        elif self.input['ForwardA'] == 'MEM':
            if self.input['MEM_MemToReg'] == 1:
                A = self.input['MEM_LMD']
            else:
                A = self.input['MEM_ALUResult']
        if self.input['ForwardB'] == 'EX':
            B = self.input['EX_ALUResult']
        elif self.input['ForwardB'] == 'MEM':
            if self.input['MEM_MemToReg'] == 1:
                B = self.input['MEM_LMD']
            else:
                B = self.input['MEM_ALUResult']
        self.data.update_value("MemData", B)
        if self.input['ID_ALUSrc'] == 'imm':
            B = self.input['ID_imm']

        try:
            if self.input['ID_ALUOp'] == 'sum':
                self.data.update_value("ALUResult", A + B)
            elif self.input['ID_ALUOp'] == 'sub':
                self.data.update_value("ALUResult", A - B)
        except:
            pass
