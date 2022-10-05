contatos = {"helgannick@gmail.com": {"nome": "Marcos", "telefone": "3333-2221"}}

copia = contatos.copy()
copia["helgannick@gmail.com"] = {"nome": "Gui"}

print(contatos["helgannick@gmail.com"])  # {"nome": "Guilherme", "telefone": "3333-2221"}

print(copia["helgannick@gmail.com"])  # {"nome": "Gui"}