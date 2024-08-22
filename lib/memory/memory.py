class memory:
    class word:
        def __init__(self):
            self.value = (False,)
        def __str__(self):
            return str(self.value)

    def __init__(self, size):
        self.memory = [memory.word() for _ in range(size//4)]
        self.name = ""

    def read_word(self, address):
        value = self.memory[address//4].value
        #if value == (False,):
        #    err = EOFError()
        #    err.args = ("EOF",)
        #    raise err
        return value

    #def read_byte(self, address):
    #    return self.memory[address//4].value[address%4]

    def write_word(self, address, value):
        self.memory[address//4].value = value
        #print(self)

    #def write_byte(self, address, value):
    #    self.memory[address//4].value[address%4] = value

    def __repr__(self):
        s = f"{self.name}\n"
        for i, word in enumerate(self.memory):
            try:
                if word.value == (False,):
                    break
            except:
                pass
            s += f"{i*4}: {word}\n"
        return s
