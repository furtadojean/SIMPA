from enum import Enum

class instruction:
    def __init__(self):
        self.instr = ''
        self.rs1 = ''
        self.rs2 = ''
        self.rd = ''
        self.imm = 0

    def __repr__(self):
        return f'instr:{{{self.instr}}} rd:{{{self.rd}}} rs1:{{{self.rs1}}} rs2:{{{self.rs2}}} imm:{{{self.imm}}}'

class var:
    class var_type(Enum):
        WORD = 0
        ASCIZ = 1
    def __init__(self, var_type, name, value):
        self.name = name
        self.type = var_type
        self.value = value
    def __repr__(self):
        return f'({self.type.name}) {self.name}: {self.value}'

class parser:
    def __init__(self, data_mem, instr_mem):
        self.lines = []
        self.labels = {}
        self.vars = {}
        self.data_mem = data_mem
        self.data_mem_pos = 0
        self.instr_mem = instr_mem

    def read(self, content, file=True):
        if file == True:
            content = open(content, 'r').readlines()
        for line in content:
            if len(line.split()) == 0:
                continue
            if line[0] == '#':
                continue
            self.lines.append(line)

    def parse(self):
        for i, line in enumerate(self.lines):
            line = line.strip()
            if line == '':
                continue
            if line[-1] == ':':
                continue
            self.lines[i] = line.split()
        self.create_instructions()

    def create_instructions(self):
        for line in self.lines:
            if line[0] == 'asciz':
                if line[1] in self.vars:
                    continue
                v = var(var.var_type.ASCIZ, line[1], line[2].replace('"', ''))
                self.data_mem.write_word(self.data_mem_pos, v)
                self.vars[v.name] = self.data_mem_pos
                self.data_mem_pos += 4
                continue
            elif line[0] == 'word':
                if line[1] in self.vars:
                    continue
                v = var(var.var_type.WORD, line[1], int(line[2]))
                self.data_mem.write_word(self.data_mem_pos, v)
                self.vars[v.name] = self.data_mem_pos
                self.data_mem_pos += 4
                continue
            data = instruction()
            if line[0] == 'lw':
                data.instr = 'lw'
                data.rd = line[1]
                data.rs1 = line[2].split('(')[1][:-1] #)
                data.imm = int(line[2].split('(')[0]) #)
            elif line[0] == 'lb':
                data.instr = 'lb'
                data.rd = line[1]
                data.rs1 = line[2].split('(')[1][:-1] #)
                data.imm = int(line[2].split('(')[0]) #)
            elif line[0] == 'sw':
                data.instr = 'sw'
                data.rs1 = line[1]
                data.rs2 = line[2].split('(')[1][:-1] #)
                data.imm = int(line[2].split('(')[0]) #)
            elif line[0] == 'sb':
                data.instr = 'sb'
                data.rs1 = line[1]
                data.rs2 = line[2].split('(')[1][:-1] #)
                data.imm = int(line[2].split('(')[0]) #)
            elif line[0] == 'la':
                data.instr = 'la'
                data.rd = line[1]
                data.rs1 = 'zero'
                data.imm = self.vars[line[2]]
            elif line[0] == 'pint':
                data.instr = 'pint'
                data.rs1 = line[1]
                data.rs2 = 'zero'
            elif line[0] == 'pstr':
                data.instr = 'pstr'
                data.rs1 = line[1]
                data.rs2 = 'zero'
            elif line[0] == 'add':
                data.instr = 'add'
                data.rd = line[1]
                data.rs1 = line[2]
                data.rs2 = line[3]
            elif line[0] == 'addi':
                data.instr = 'addi'
                data.rd = line[1]
                data.rs1 = line[2]
                data.imm = int(line[3])

            self.instr_mem.write_instruction(data)
