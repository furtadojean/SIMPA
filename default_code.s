# Define dois inteiros e uma string
word t 4
word num 42
asciz bem_vindo "Bem Vindo!"

# Coloca o endereço da string (8) em t0
la t0 bem_vindo
pstr t0

# Coloca o endereço do primeiro inteiro (0) em t0
la t0 t
# Coloca o segundo inteiro (42) em t1
lw t1 4(t0)
# Dobra t1 (84)
add t1 t1 t1
# Substitui o segundo inteiro por t1 (num=84)
sw t1 4(t0)
pint t1

# Coloca o endereço do segundo inteiro (4) em t2
la t2 num
# Printa t2 (84)
pint t2

# Coloca o segundo inteiro (84) em t2
lw t2 0(t2)
pint t2

# Adiciona 8 a t2 (92)
addi t2 t2 8
pint t2

# Define t3 como t1 + t2
add t3 t2 t1
pint t3
