import template
import lib

import io
from contextlib import redirect_stdout


def execute(code):
    result_info = ""
    memory_info = ""
    execution_info = ""

    alu = template.ALU()
    pc = template.PC()
    cu = template.CU()
    data_memory = template.c_data_memory()
    instruction_memory = template.c_instr_memory()
    forwarding_unit = template.forwarding_unit()
    hazard_unit = template.hazard_unit()
    registers_read = template.registers()
    registers_write = template.registers()

    alu.setup(forwarding_unit)
    pc.setup(hazard_unit)
    cu.setup(hazard_unit)
    data_memory.setup()
    instruction_memory.setup(pc)
    forwarding_unit.setup()
    hazard_unit.setup(pc)
    registers_read.setup(template.if_id())
    registers_write.setup(template.mem_wb())

    print_unit = template.print_unit()
    print_unit.setup(data_memory.mem, template.registers.bank)

    template.if_id().setup([pc, instruction_memory])
    template.id_ex().setup([cu, registers_read, template.if_id()])
    template.ex_mem().setup([alu, template.id_ex()])
    template.mem_wb().setup([data_memory, template.ex_mem()])


    parser = lib.parser(data_memory.mem, instruction_memory.mem)
    parser.read(code, file=False)
    parser.parse()

    intermediate_registers = [template.if_id(), template.id_ex(), template.ex_mem(), template.mem_wb()]
    intermediate_register_names = ["if_id", "id_ex", "ex_mem", "mem_wb"]
    clock = 0
    def one_clock():
        nonlocal clock, pc
        pc.on_clock()
        print("-------------------------------------------------------------")
        print("PC: ", pc.data.get_value("address"))
        for intermediate_register in intermediate_registers:
            print("Ready: ", intermediate_register_names[intermediate_registers.index(intermediate_register)])
            intermediate_register.ready()
            print(intermediate_register.data)
            print()
        for intermediate_register in intermediate_registers:
            intermediate_register.on_clock()
        clock += 1
    while True:
        with io.StringIO() as buf, redirect_stdout(buf):
            one_clock()
            execution_info += buf.getvalue()
        try:
            if clock > 1 and template.mem_wb.data.get_value("IR") == (False,):
                break
        except:
            pass
    for intermediate_register in intermediate_registers:
        intermediate_register.data.clean()
        intermediate_register.input.clean()

    result_info = print_unit.buffer
    with io.StringIO() as buf, redirect_stdout(buf):
        print(registers_read.bank)
        print(instruction_memory.mem)
        print(data_memory.mem)
        memory_info = buf.getvalue()
    return result_info, execution_info, memory_info

if __name__ == "__main__":
    content = open("default_code.s").readlines()
    for info in execute(content):
        print(info)
