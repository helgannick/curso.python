from telnetlib import STATUS


saldo = 1500
saque = 500

status = 'Sucesso' if  saldo > = saque else 'Falha'

print(f'{status} ao realizar o saque!')