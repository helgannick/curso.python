contatos = {"guilherme@gmail.com": {"nome": "Marcos", "telefone": "3333-2221"}}

resultado = contatos.pop("helgannick@gmail.com")  # {'nome': 'Guilherme', 'telefone': '3333-2221'}
print(resultado)

resultado = contatos.pop("helgannick@gmail.com", {})  # {}
print(resultado)