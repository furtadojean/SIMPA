from lib import bank
from lib import component

class register_bank(bank):
    def __init__(self):
        super().__init__()
        self.setup_registers( ['zero',
                               't0',
                               't1',
                               't2',
                               't3',
                               't4',
                               't5',
                               't6',
                               ]
                             )


class registers(component):
    bank = register_bank()
    def __init__(self):
        super().__init__()

    def setup(self, inter_reg):
        self.add_dependency(inter_reg)

    def _compute(self):
        super()._compute()
        if self.input['MEM_RegWrite'] == 1:
            if self.input['MEM_MemToReg'] == 1:
                self.bank[self.input['MEM_IR'].rd] = self.input['MEM_LMD']
            else:
                self.bank[self.input['MEM_IR'].rd] = self.input['MEM_ALUResult']
        else:
            self.data.update_value("A", self.bank[self.input['IF_IR'].rs1])
            self.data.update_value("B", self.bank[self.input['IF_IR'].rs2])
            self.data.update_value("imm", self.input['IF_IR'].imm)
