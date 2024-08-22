class bank:
    def __init__(self):
        self.registers = {}

    def setup_registers(self, names):
        for name in names:
            self.registers[name] = 0

    def __getitem__(self, name):
        try:
            return self.registers[name]
        except:
            return None

    def __setitem__(self, name, value):
        if name in ['zero']:
            return
        self.registers[name] = value

    def __repr__(self):
        s = "REGISTERS\n"
        for name, value in self.registers.items():
            s += f"{name}: {value}\n"
        return s
