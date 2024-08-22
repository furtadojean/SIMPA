from lib import component
from .intermediate_registers import if_id, id_ex

class hazard_unit(component):
    def __init__(self):
        super().__init__()

    def setup(self, pc):
        self.add_dependency(if_id())
        self.add_dependency(id_ex())
        self.pc = pc

    def _compute(self):
        super()._compute()
        if self.input['ID_MemRead'] == 1 and \
            (self.input['ID_IR'].rd == self.input['IF_IR'].rs1 or \
            self.input['ID_IR'].rd == self.input['IF_IR'].rs2):
                #self.pc.update_value("PC", self.input['ID_PC'])
                info = if_id.data
                self.data.update_value("stall", 1)
                if_id.data = info
        else:
            self.data.update_value("stall", 0)
