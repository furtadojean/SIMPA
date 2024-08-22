from lib import component
from .intermediate_registers import if_id

class CU(component):
    def __init__(self):
        super().__init__()
        self.reset()

    def setup(self, hazard_unit):
        self.add_dependency(if_id())
        self.add_dependency(hazard_unit)

    def reset(self):
        self.data.update_value("ALUOp", "")
        self.data.update_value("ALUSrc", "")
        self.data.update_value("MemRead", 0)
        self.data.update_value("MemWrite", 0)
        self.data.update_value("Branch", 0)
        self.data.update_value("RegWrite", 0)
        self.data.update_value("MemToReg", 0)
        self.data.update_value("Print", 0)


    def _compute(self):
        super()._compute()
        #self.instr = ''
        #self.rs1 = 0
        #self.rs2 = 0
        #self.rd = 0
        #self.imm = 0
        self.reset()
        if self.input['stall'] == 1:
            return
        '''
        lw reg dist(addr)
        lb reg dist(addr)
        sw reg dist(addr)
        sb reg dist(addr)
        la reg name

        asciz name "string"
        word name value

        pint reg
        pstr reg

        add reg reg reg
        addi reg reg imm

        beq reg reg label
        j label
        '''


        data = self.input['IF_IR']
        if data.instr in ['add', 'addi']:
            self.data.update_value("ALUOp", "sum")

        if data.instr in ['pint', 'pstr']:
            self.data.update_value("ALUOp", "sum")
            self.data.update_value("Print", 1)

        if data.instr in ['lw', 'lb', 'sw', 'sb', 'la', 'addi']:
            self.data.update_value("ALUSrc", "imm")
            self.data.update_value("ALUOp", "sum")
        else:
            self.data.update_value("ALUSrc", "reg")

        if data.instr in ['lw', 'lb']:
            self.data.update_value("MemRead", 1)
        if data.instr in ['sw', 'sb']:
            self.data.update_value("MemWrite", 1)

        if data.instr in ['beq', 'j']:
            self.data.update_value("Branch", 1)

        if data.instr in ['beq']:
            self.data.update_value("AluOp", "sub")

        if data.instr in ['lw', 'lb', 'la', 'add', 'addi']:
            self.data.update_value("RegWrite", 1)

        if data.instr in ['lw', 'lb']:
            self.data.update_value("MemToReg", 1)
