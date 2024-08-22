from lib import get_intermediate_register

if_id = get_intermediate_register()
id_ex = get_intermediate_register()
ex_mem = get_intermediate_register()
mem_wb = get_intermediate_register()

if_id.data.prefix = "IF"
id_ex.data.prefix = "ID"
ex_mem.data.prefix = "EX"
mem_wb.data.prefix = "MEM"
