from lib import component
from .intermediate_registers import ex_mem

class PC(component):
    def __init__(self):
        super().__init__()
        self.data.add_value("address", 0)
        self.address_tmp = 0

    def setup(self, hazard_unit):
        self.add_dependency(ex_mem())
        self.add_dependency(hazard_unit)

    def _compute(self):
        super()._compute()
        if self.input['EX_Branch'] == 1:
            self.address_tmp = self.input['EX_BranchTarget']
            #self.data.update_value("addressTmp", self.input['EX_BranchTarget'])
        else:
            self.address_tmp = self.data.get_value("address") + 4
            #self.data.update_value("addressTmp", self.data.get_value("address")+4)

        if self.input['stall'] == 1:
            #self.data.update_value("addressTmp", self.data.get_value("address"))
            self.address_tmp = self.data.get_value("address")
            #self.data.update_value("address", self.data.get_value("address"))

    def on_clock(self):
        #self.data.update_value("address", self.data.get_value("addressTmp"))
        #print(self.data.get_value("address"), self.address_tmp)
        self.data.update_value("address", self.address_tmp)
