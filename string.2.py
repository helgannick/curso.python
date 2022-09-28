nome = 'marcos'
idade = 30
profissão = 'programador'
linguagem = 'python'

dados = {'nome': 'marcos', 'idade': 30}

print('Nome: %s Idade: %d' % (nome, idade))
print('Nome: {} Idade: {}'.format(nome, idade))
print('Nome: {1} Idade: {0}'.format(idade, nome))
print('Nome: {0} Idade: {1} Nome: {0} {0}'.format(nome, idade))
print('Nome: {nome} Idade: {idade}'.format(nome=nome, idade=idade))
print('Nome: {nome} Idade: {idade}'.format(**dados))