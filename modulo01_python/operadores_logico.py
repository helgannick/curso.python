#AND = para ser True tudo tem que ser True
#OR = para ser True apenas um tem que ser True

print(True and True and True)
print(True and False and True)
print(False and False and False)
print(True or True and True)
print(True or False or False)
print(False or False and False)


saldo = 1000
saque = 320
limite = 250
conta_especial = True

exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(exp)
exp_2 = (saldo >=  saque and saque <= limite) or (conta_especial and saldo >= saque)
print(exp_2)