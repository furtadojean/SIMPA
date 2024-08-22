from lib import component
from .intermediate_registers import id_ex

class branch_adder(component):
    def __init__(self):
        super().__init__()
        self.data.add_value("BranchTarget", 0)

    def setup(self):
        self.add_dependency(id_ex())

    def _compute(self):
        super()._compute()
        self.data.update_value("BranchTarget", self.input['ID_address'] + self.input['ID_imm'])
